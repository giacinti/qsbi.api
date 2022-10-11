from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, check_all_non_null


class Currency(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    nickname: Optional[str]
    code: Optional[str]


class CurrencyCreate(Currency):
    @root_validator
    def CurrencyCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'name', 'nickname', 'code')


class CurrencyRead(BaseAny):
    id: Optional[int]
    name: Optional[str]
    nickname: Optional[str]
    code: Optional[str]


class CurrencyUpdate(Currency, BaseAny):
    pass


class CurrencyDelete(CurrencyRead):
    pass
