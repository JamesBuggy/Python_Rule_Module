from .models.rule_result import RuleResult
from .rules.base_rule import BaseRule
from typing import Type

class RuleChain:

    def __init__(self):
        self.is_successful = True

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
        result: RuleResult = rule().execute()
        self.is_successful = result.is_successful