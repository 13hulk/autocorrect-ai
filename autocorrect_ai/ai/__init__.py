from kit.proxy import ProxyObject, Sentinel

from .llm import Llm
from .ollama import OllamaConfig, OllamaModel
from .templates import Templates

__all__ = ["TEMPLATES", "LLM", "Templates", "init_templates", "init_llm"]

_sentinel_templates = Sentinel()
TEMPLATES: Templates = ProxyObject(_sentinel_templates)

_sentinel_llm = Sentinel()
LLM: Llm = ProxyObject(_sentinel_llm)


def init_templates():
    global _sentinel_templates

    _sentinel_templates.obj: Templates = Templates()


def init_llm():
    global _sentinel_llm

    _sentinel_llm.obj: OllamaModel = OllamaModel(
        template=TEMPLATES.PROMPT_TEMPLATE_FIX_TEXT, config=OllamaConfig()
    )
