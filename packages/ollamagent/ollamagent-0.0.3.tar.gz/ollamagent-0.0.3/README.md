# OllamAgent

`OllamAgent` is a wrapper aroundn Ollama API. Ollama is a mini framework for consuming, managing and maintaining SOTA (State of the Art) Large Language Models that have been Quantaized and optimized for deployment on edge devices, there is no need for 'OpenAI' or 'HuggingFace' API keys, or even 'API_KEY' for that matter, you can run these models within your own devices ensuring data privacy, security and most importantly accesibility to this cutting edge technology for people with limited resources.
It implements an Agent | Tools mini-framework that simplifies the ussage of the full set of features of the supported models (Currently only Mistral7B is supported).

## Installation

```bash
pip install ollamagent
```

## Usage

```python
from ollamagent import APIClient, Agent, Tool

# Implementing an integration with a third party API
class MyAPI(APIClient):
	base_url = "https://api.myapi.com"
	headers = {
		"Authorization": "Bearer MY_API_KEY"
	}
 
	async def my_api_method(self, data):
		return await self.post("/my-api-method", data)

# Implementing a tool
class MyTool(Tool):
	data: dict

	@property
	def api(self):
		return MyAPI()
	
	async def run(self):
		return await self.api.my_api_method(self.data)

# Instantiating the agent
agent = Agent(tools=[MyTool])

# Interacting with the agent
async def main():
	print(await agent.chat(message="Hello! Are you there?"))
	>>> "Hello! I'm here, how can I help you?"
	print(await agent.run_tool("MyTool", data={"key": "value"}))
	>>> {"response": "from", "my": "api"}
 
asyncio.run(main())
```