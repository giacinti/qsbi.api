from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null


class AccountType(BaseQsbi):
    id: Optional[int]
    name: Optional[str]


class AccountTypeCreate(AccountType):
    @root_validator
    def AccountTypeCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'name')


class AccountTypeRead(BaseAny):
    id: Optional[int]
    name: Optional[str]


class AccountTypeUpdate(AccountType, BaseIdOrName):
    pass


class AccountTypeDelete(AccountTypeRead):
    pass
