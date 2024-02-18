from enum import Enum
from typing import List, Optional, Tuple, Union

import antimatter.client as openapi_client


class CapabilityOperator(str, Enum):
    In = "In"
    NotIn = "NotIn"
    Exists = "Exists"
    NotExists = "NotExists"


class CapabilityRules:
    def __init__(self, *rules):
        self._rules: List[Tuple[str, CapabilityOperator, List[str]]] = list(rules)

    def with_rule(
        self,
        name: str,
        operator: Optional[Union[CapabilityOperator, str]],
        values: Optional[List[str]] = None,
    ) -> "CapabilityRules":
        if operator is not None:
            operator = CapabilityOperator(operator)
        if values is None:
            values = []
        self._rules.append((name, operator, values))
        return self

    def build(self) -> openapi_client.CapabilityRule:
        return openapi_client.CapabilityRule(
            match_expressions=[
                openapi_client.CapabilityRuleMatchExpressionsInner(
                    name=rule[0],
                    operator=rule[1] and rule[1].value,
                    values=rule[2],
                ) for rule in self._rules
            ]
        )
