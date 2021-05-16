from typing import Any
from ..models.rule_result import RuleResult

class BaseRule:

    required_inputs: list[str]

    def __init__(self, **inputs: Any) -> None:
        self._validateRequiredInputs(**inputs)
        self.inputs: dict[str, Any] = inputs

    def execute(self) -> RuleResult:
        raise NotImplementedError(f'{self.__class__.__name__} - Required function not implemented: execute')

    def _validateRequiredInputs(self, **inputs: Any) -> None:
        for input_ in self.required_inputs:
            if input_ not in inputs:
                raise Exception(f'{self.__class__.__name__} - Required input missing: {input_}')