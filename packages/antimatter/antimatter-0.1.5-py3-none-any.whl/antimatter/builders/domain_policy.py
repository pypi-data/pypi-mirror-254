from enum import Enum


class Operation(str, Enum):
    Edit = "edit"
    View = "view"
    Use = "use"


class Result(str, Enum):
    Allow = "allow"
    Deny = "deny"
