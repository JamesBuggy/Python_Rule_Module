from enum import Enum
from typing import Any
from ..models.rule_result import RuleResult
from ..enums.rule_error import RuleError

class BaseRule:

    required_inputs: list[str]
    optional_inputs: list[str]

    def __init__(self, **inputs: Any) -> None:
        self._validateRequiredInputs(**inputs)
        self.inputs: dict[str, Any] = inputs
        self.outputs: dict[str, Any] = dict()
        self.errors: dict[Enum, list[str]] = dict()

    def execute(self) -> RuleResult:
        print(f'{self.__class__.__name__} - Starting with inputs: {self.inputs}')
        try:
            self._execute()
        except Exception as e:
            self.errors[RuleError.UNKNOWN] = [str(e)]
        result = RuleResult(not self.errors, errors=self.errors, **self.outputs)
        print(f'{self.__class__.__name__} - Completed with results: {result.__dict__}')
        return result

    def _validateRequiredInputs(self, **inputs: Any) -> None:
        for input_ in self.required_inputs:
            if input_ not in inputs:
                raise Exception(f'{self.__class__.__name__} - Required input missing: {input_}')

    def _execute(self) -> None:
        raise NotImplementedError(f'{self.__class__.__name__} - Required function not implemented: _execute(self)')