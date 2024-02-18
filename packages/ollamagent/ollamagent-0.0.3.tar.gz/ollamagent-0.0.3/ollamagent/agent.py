"""
Agent module.
Agent is based on mistral-7B-instruct-2.0 quantized to 4 bits 
it can be run locally and interacted with via a chat interface.
The agent can be used to run tools based on user input.
The agent is trained to provide useful responses and guidance to the user.
"""

import json as json_module
from functools import cached_property
from typing import AsyncIterator, Iterable, Literal, Mapping, Protocol, Type, TypeVar

from jinja2 import Template
from ollama import AsyncClient  # type: ignore
from pydantic import BaseModel, Field

from ._prompt import CHAT_TEMPLATE, RUN_TEMPLATE
from .proxy import LazyProxy
from .tool import Tool, ToolOutput

T_co = TypeVar("T_co", covariant=True)


class Message(BaseModel):
    """
    Represents a message with a role and content.

    Attributes:
        role (Literal["user", "assistant"]): The role of the message sender.
        content (str): The content of the message.
    """

    role: Literal["user", "assistant"]
    content: str


class AgentProtocol(Protocol[T_co]):
    """A protocol for an agent that interacts with users and performs tool calls based on user input."""

    messages: list[Message]
    model: str
    tools: Iterable[Type[Tool]]

    async def chat(
        self, *, message: str, stream: bool = True
    ) -> AsyncIterator[Message] | Message:
        """Chat with the agent."""
        raise NotImplementedError

    async def run(self, *, message: str) -> ToolOutput:
        """Executes a tool based on natural language input."""
        raise NotImplementedError

    def __load__(self) -> T_co:
        """Loads the AsyncClient."""
        raise NotImplementedError


class BaseAgent(AgentProtocol[T_co], LazyProxy[T_co]):
    """Base class for an agent."""

    messages: list[Message] = []
    model: str
    tools: Iterable[Type[Tool]] = Tool.__subclasses__()

    async def chat(
        self, *, message: str, stream: bool = True
    ) -> AsyncIterator[Message] | Message:
        """Chat with the agent."""
        raise NotImplementedError

    async def run(self, *, message: str) -> ToolOutput:
        """Executes a tool based on natural language input."""
        raise NotImplementedError


class Agent(BaseModel, BaseAgent[AsyncClient]):
    """An agent that interacts with users and performs tool calls based on user input.

    Attributes:
        messages (list[Message]): List of messages exchanged between the user and the agent.
        model (str): The model used by the agent.
        tools (list[Type[Tool[Any]]]): List of available tool classes.

    Methods:
        chat: Chat Stream with the agent as an Q&A chatbot. Can implement Retrieval Augmented Generation (RAG) for better responses by using the `chat_template` attribute to render the context and instructions for the agent.
        run: Runs a tool based on user's message. The agent picks a tool from the list of definitions available, otherwise it returns a chat `Message` object. The agent sends an inferred json object based on the tool definition and user input to the Tool class, which call it's constructor with the parsed json object. The Tool executes the logic implemented on it's run method and returns the output as a ToolOutput object with the following structure:
        ```json
        {
            "role": "tool_name",
            "content": "tool_output"
        }
        ```
        The agent returns the ToolOutput object to the user.
        __load__: Load the AsyncClient.
        chat_template: The template used for enabling the agent with context and instructions for responding to user's messages.
        run_template: The template used for generating the `function_calling` prompt for the model.
        __call__: Runs a specific tool class based on a user message.
    """

    messages: list[Message] = []
    model: str = Field(
        default="mistral:instruct"
    )  # [TODO] Implement other models: `llama2`, `starcoder`
    tools: Iterable[Type[Tool]] = Tool.__subclasses__()

    @cached_property
    def run_template(self):
        """The template used for generating the message sent to the agent. Crafted using prompt engineering to guide the model to infer the schema for performing tool calls based on user's message."""
        # [TODO] Implement other models: `llama2`, `starcoder`
        return Template(RUN_TEMPLATE, enable_async=True)

    @cached_property
    def chat_template(self):
        """The template used for enabling the agent with context and instructions for responding to user's messages."""
        # [TODO] Implement other models: `llama2`, `starcoder`
        return Template(CHAT_TEMPLATE, enable_async=True)

    def __load__(self):
        """Load the AsyncClient."""
        return AsyncClient()

    async def chat(
        self, *, message: str, stream: bool = True
    ) -> AsyncIterator[Message] | Message:
        """
        Chat with the agent.

        Args:
            message (str): The message sent to the agent.
            stream (bool): Whether the response should be streamed or not.

        Returns:
            The response from the agent.
            (AsyncIterator[Message]): If stream is True.
            (Message): If stream is False.
        Raises:
            ValueError: If the response doesn't contain any content.
        """
        self.messages.append(Message(role="user", content=message))
        response = await self.__load__().chat(
            model=self.model,
            stream=stream,
            messages=[m.model_dump() for m in self.messages],  # type: ignore
        )
        if stream:
            assert isinstance(response, AsyncIterator)

            async def iterator():
                string = ""
                async for choice in response:
                    content = choice["message"].get("content")
                    if content and isinstance(content, str):
                        string += content
                        yield Message(role="assistant", content=content)
                self.messages.append(Message(role="assistant", content=string))

            return iterator()

        assert isinstance(response, Mapping)
        content = response["message"].get("content")
        if content and isinstance(content, str):
            model_output = Message(role="assistant", content=content)
            self.messages.append(model_output)
            return model_output
        raise ValueError("No content in response")

    async def run(self, *, message: str) -> ToolOutput:
        """Executes a tool based on natural language input.
        It works as follows:
        1. The user provides a message.
        2. The agent picks a tool from the list of definitions available, otherwise it returns a chat `Message` object.
        3. The agent sends an inferred json object based on the tool definition and user input to the Tool class, which call it's constructor with the parsed json object.
        4. The Tool executes the logic implemented on it's run method and returns the output as a ToolOutput object with the following structure:

        ```json
        {
            "role": "tool_name",
            "content": "tool_output"
        }
        ```

        5. The agent returns the ToolOutput object to the user.

        Args:
            message (str): The message sent to the agent.

        Returns:
            ToolOutput: The output of the tool.
        """
        message = await self.run_template.render_async(
            message=message,
            definitions=[klass.definition() for klass in self.tools],
        )
        response = await self.chat(
            message=message,
            stream=False,
        )
        assert isinstance(response, Message)
        data = json_module.loads(response.content)
        tool = next(
            klass(**data["tool"]["parameters"])
            for klass in self.tools
            if klass.__name__ == data["tool"]["name"]
        )
        return await tool()
