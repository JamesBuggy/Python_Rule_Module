from typing import Any, Type
from .models.rule_result import RuleResult
from .enums.rule_error_type import RuleErrorType
from .rules.base_rule import BaseRule

class RuleChain:

    def __init__(self, **inputs: Any) -> None:
        self.is_successful = True
        self.inputs: dict[str, Any] = inputs
        self.outputs: dict[str, Any] = dict()
        self.errors: dict[RuleErrorType, list[str]] = dict()

    def execute(self, rule: Type[BaseRule]) -> 'RuleChain':
        self._execute_rule(rule)
        return self

    def if_successful(self, rule: Type[BaseRule]) -> 'RuleChain':
        if self.is_successful:
            self._execute_rule(rule)
        return self

    def if_failed(self, rule: Type[BaseRule]) -> 'RuleChain':
        if not self.is_successful:
            self._execute_rule(rule, False)
        return self

    def _execute_rule(self, rule: Type[BaseRule], update_chain_status: bool = True) -> None:
        rule_inputs: dict[str, Any] = { required_input: (self.inputs | self.outputs)[required_input] for required_input in rule.required_inputs }
        result: RuleResult = rule(**rule_inputs).execute()
        self.outputs = self.outputs | result.outputs
        self.errors = self._combine_errors(self.errors, result.errors)
        self.outputs['errors'] = self.errors
        if update_chain_status:
            self.is_successful = result.is_successful

    def _combine_errors(self, current_errors: dict[RuleErrorType, list[str]], new_errors: dict[RuleErrorType, list[str]]) -> dict[RuleErrorType, list[str]]:
        combined_errors: dict[RuleErrorType, list[str]] = {key:[] for key in current_errors.keys() | new_errors.keys()}
        for key in current_errors.keys():
            combined_errors[key] = combined_errors[key] + current_errors[key]
        for key in new_errors.keys():
            combined_errors[key] = combined_errors[key] + new_errors[key]
        return combined_errors