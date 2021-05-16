from typing import Any

class RuleResult:

    def __init__(self, is_successful: bool, **outputs: Any):
        self.is_successful = is_successful
        self.outputs: dict[str, Any] = outputs