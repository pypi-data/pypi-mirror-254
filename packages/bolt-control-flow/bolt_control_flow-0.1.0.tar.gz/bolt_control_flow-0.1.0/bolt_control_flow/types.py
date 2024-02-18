from dataclasses import dataclass
from enum import Enum, auto
from types import NotImplementedType
from typing import Any, Optional, TypeAlias

CaseResult: TypeAlias = tuple[Any, tuple[Any, ...]]
CasePartialResult: TypeAlias = CaseResult | NotImplementedType


# TODO: more specific type for case object when representing match cases
Case: TypeAlias = bool | Any


class BranchType(Enum):
    IF_ELSE = auto()
    MATCH = auto()

    @property
    def helper(self) -> str:
        return f"multibranch_{self.name}"


@dataclass(frozen=True)
class BranchInfo:
    branch_type: BranchType
    parent_cases: Optional[Any]


@dataclass
class BinaryLogicalFallback:
    right: Any


class WrappedCases:
    """Marker class to indicate that it is safe for nested conditions to use return without making new functions

    i.e. there are no commands after the cases that must be run
    """
