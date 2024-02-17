from garak.generators.replicate import ReplicateGenerator, InferenceEndpoint

# from ..engine.config import AgentConfig, _get_default_agent_config
from ..engine.config import _get_default_agent_config
from ..utils import block_print, enable_print


class ReplicateAPI(ReplicateGenerator):
    def __init__(self, name, generations: float = 10):
        # def __init__(self, name, generations: float = 10, config: AgentConfig=None):
        # block_print()
        super().__init__(name, generations)
        enable_print()
        self.family = "Replicate"
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


class ReplicateEndpoint(InferenceEndpoint):
    def __init__(self, name, generations: float = 10):
        # def __init__(self, name, generations: float = 10, config: AgentConfig=None):
        # block_print()
        super().__init__(name, generations)
        # enable_print()
        self.family = "Replicate"
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


# more stable option is enabled by default
default_class = "ReplicateEndpoint"
