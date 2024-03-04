from string import Template

import httpx

from .llm import Llm


class OllamaConfig:
    ENDPOINT = "http://localhost:11434/api/generate"
    MODEL = "mistral:7b-instruct-v0.2-q4_K_S"
    KEEP_ALIVE = "5m"
    STREAM = False

    def to_dict(self) -> dict:
        return {
            "model": self.MODEL,
            "keep_alive": self.KEEP_ALIVE,
            "stream": self.STREAM,
        }


class OllamaModel(Llm):
    def __init__(self, template: Template, config: OllamaConfig):
        self.template: Template = template
        self.config: OllamaConfig = config

    def generate(self, text: str) -> str:
        prompt = self.template.substitute(text=text)
        response = httpx.post(
            self.config.ENDPOINT,
            json={"prompt": prompt, **self.config.to_dict()},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        if response.status_code != 200:
            print("Error", response.status_code)
            return None

        return self.sanitize(response.json()["response"])

    def sanitize(self, text: str) -> str:
        text = text.strip()

        if text[0] in ('"', "'"):
            text = text[1:]

        if text[-1] in ('"', "'"):
            text = text[:-1]

        return text
