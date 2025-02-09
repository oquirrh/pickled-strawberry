import requests
import os
from dotenv import load_dotenv

class LlmInterface:
    def __init__(self, model):
        load_dotenv()
        self.model = model
        #self.OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
        self.OPENROUTER_API_KEY = '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'

    def query(self, query, context):
        """
            Generate a response using OpenRouter API.

            :param query: User's question
            :param context: Retrieved documents
            :param model: LLM model to use (e.g., "mistralai/mistral-7b-instruct", "meta-llama/llama-2-13b-chat")
            :return: LLM response
            """

        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": [
                {"role": "system",
                 "content": "You are an AI assistant that answers queries using the provided context."},
                {"role": "user", "content": f"Context: {context}\n\nQuery: {query}"}
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"
