from typing import Any, Type
from .models.rule_result import RuleResult
from .rules.base_rule import BaseRule

class RuleChain:

    def __init__(self, **inputs: Any) -> None:
        self.is_successful = True
        self.inputs: dict[str, Any] = inputs
        self.outputs: dict[str, Any] = dict()

    def execute(self, rule: Type[BaseRule]) -> 'RuleChain':
        self._execute(rule)
        return self

    def if_successful(self, rule: Type[BaseRule]) -> 'RuleChain':
        if self.is_successful:
            self.execute(rule)
        return self

    def if_failed(self, rule: Type[BaseRule]) -> 'RuleChain':
        if not self.is_successful:
            self.execute(rule)
        return self

    def _execute(self, rule: Type[BaseRule]) -> None:
        rule_inputs = {**self.inputs, **self.outputs}
        result: RuleResult = rule(**rule_inputs).execute()
        self.is_successful = result.is_successful
        self.outputs = {**self.outputs, **result.outputs}