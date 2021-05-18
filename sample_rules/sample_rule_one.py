from typing import Any
from rules_module import BaseRule

class SampleRuleOne(BaseRule):

    required_inputs: list[str] = []

    def __init__(self, **inputs: Any) -> None:
        super().__init__(**inputs)

    def _execute(self) -> None:
        self.outputs['example_output_1'] = 'example_output_value'