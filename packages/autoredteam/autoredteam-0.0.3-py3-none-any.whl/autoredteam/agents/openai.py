import os
from garak.generators.openai import OpenAIGenerator
from ..engine.config import _get_default_agent_config
from ..utils import block_print, enable_print


class OpenaiAgent(OpenAIGenerator):
    def __init__(self, name, generations: float = 10):
        # def __init__(self, name, generations: float = 10, config: AgentConfig=None):

        os.environ["OPENAI_API_TOKEN"] = os.getenv("OPENAI_API_TOKEN")
        # block_print()
        super().__init__(name, generations)
        # enable_print()
        self.family = "OpenAI"
        # if config is None:
        config = _get_default_agent_config(family="", name=self.name)
        for field in [
            "max_tokens",
            "presence_penalty",
            "temperature",
            "top_k",
            "seed",
            "presence_penalty",
            "supports_multiple_generations",
        ]:
            if hasattr(config, field):
                setattr(self, field, getattr(config, field))


default_class = "OpenaiAgent"
