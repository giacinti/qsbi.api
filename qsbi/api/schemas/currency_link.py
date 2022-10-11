from datetime import datetime
from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_all_non_null


class CurrencyLink(BaseQsbi):
    id: Optional[int]
    cur1_id: Optional[int]
    cur2_id: Optional[int]
    rate: Optional[float]
    date: Optional[datetime]
    log_id:  Optional[int]


class CurrencyLinkCreate(CurrencyLink):
    @root_validator
    def CurrencyLinkCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'cur1', 'cur2', 'log')


class CurrencyLinkRead(BaseAny):
    id: int


class CurrencyLinkUpdate(CurrencyLink, BaseId):
    pass


class CurrencyLinkDelete(CurrencyLinkRead):
    pass
