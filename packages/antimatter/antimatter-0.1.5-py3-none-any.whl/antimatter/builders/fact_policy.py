from enum import Enum
from typing import List, Optional, Tuple, Union

import antimatter.client as openapi_client


class FactOperator(str, Enum):
    Exists = "Exists"
    NotExists = "NotExists"


class FactArgumentSource(str, Enum):
    DomainIdentity = "domainIdentity"
    Literal = "literal"


class FactPolicyArgument:
    def __init__(
        self,
        source: Union[str, FactArgumentSource],
        capability: str,
        any_value: Optional[bool] = None,
        value: Optional[str] = None,
    ):
        self._source = FactArgumentSource(source)
        self._capability = capability
        self._any = any_value
        self._value = value

    def build(self) -> openapi_client.FactPolicyRulesInnerArgumentsInner:
        return openapi_client.FactPolicyRulesInnerArgumentsInner(
            any=self._any,
            source=self._source.value,
            capability=self._capability,
            value=self._value,
        )


class FactPolicies:
    def __init__(self):
        self._policies: List[Tuple[FactOperator, str, List[FactPolicyArgument]]] = []

    def with_policy(
        self,
        name: str,
        operator: Union[FactOperator, str],
        *policies: FactPolicyArgument,
    ) -> "FactPolicies":
        self._policies.append((FactOperator(operator), name, list(policies)))
        return self

    def build(self) -> List[openapi_client.FactPolicyRulesInner]:
        return [openapi_client.FactPolicyRulesInner(
            operator=policy[0].value,
            name=policy[1],
            arguments=[arg.build() for arg in policy[2]],
        ) for policy in self._policies]
