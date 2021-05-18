from typing import Any
from rules_module import BaseRule

class SampleRuleTwo(BaseRule):

    required_inputs: list[str] = ['example_output_1']

    def __init__(self, **inputs: Any) -> None:
        super().__init__(**inputs)

    def _execute(self) -> None:
        self.outputs['example_output_2'] = 'example_output_value'