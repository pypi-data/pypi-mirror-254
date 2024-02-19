import yaml
from typing import Any

import yaml
from typing import Any, List

def _get_base_dir() -> str:
    import os
    return os.path.dirname(os.path.abspath(__file__)) + "/../.."

class InstructionRegistry:
    def __init__(self, yaml_file_paths: List[str]):
        self._registry = {}
        for yaml_file_path in yaml_file_paths:
            with open(f"{_get_base_dir()}/{yaml_file_path}", 'r') as file:
                self._registry.update(yaml.safe_load(file))

    def get(self, str_name: str) -> Any:
        return self._registry.get(str_name)

    def __getattr__(self, name: str) -> Any:
        if name in self._registry:
            return self._registry[name]
        raise AttributeError(f"No such attribute: {name}")

    def __iter__(self):
        return iter(self._registry)

# Create a global instance of the registry
instruction_registry = InstructionRegistry(['llm_party/attendee/default/default_instruction.yaml', 'llm_party/attendee/custom/custom_instruction.yaml'])
