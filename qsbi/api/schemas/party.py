from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null


class Party(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    desc: Optional[str]


class PartyCreate(Party):
    @root_validator
    def PartyCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'name')


class PartyRead(BaseAny):
    id: Optional[int]
    name: Optional[str]


class PartyUpdate(Party, BaseIdOrName):
    pass


class PartyDelete(PartyRead):
    pass
