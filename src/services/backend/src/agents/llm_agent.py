import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from src.config import API_TOGETHER_LLAMA_API_KEY

API_TOGETHER_LLAMA_URL = "https://api.together.xyz/v1/chat/completions"
API_TOGETHER_LLAMA_MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"


class LLMAgent:
    def __init__(
        self,
        model: str = API_TOGETHER_LLAMA_MODEL,
        url: str = API_TOGETHER_LLAMA_URL,
        api_key: str = API_TOGETHER_LLAMA_API_KEY,
    ):
        self.model = model
        self.url = url
        self.api_key = api_key

    @retry(
        stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=60)
    )
    async def get_completion(self, prompt: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                },
                timeout=httpx.Timeout(120),
            )
            response.raise_for_status()
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"]


llama_agent = LLMAgent()
