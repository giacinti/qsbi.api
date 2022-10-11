from datetime import datetime
from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_all_non_null


class Transact(BaseQsbi):
    id: Optional[int]
    account_id: Optional[int]
    transaction_date: Optional[datetime]
    value_date: Optional[datetime]
    party_id: Optional[int]
    category_id: Optional[int]
    sub_category_id: Optional[int]
    notes: Optional[str]
    amount: Optional[float]
    currency_id: Optional[int]
    exchange_rate: Optional[float]
    exchange_fees: Optional[float]
    payment_id: Optional[int]
    master_id: Optional[int]
    reconcile_id: Optional[int]
    log_id: Optional[int]


class TransactCreate(Transact):
    @root_validator
    def TransactCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'account', 'log')
    pass


class TransactRead(BaseAny):
    id: int


class TransactUpdate(Transact, BaseId):
    pass


class TransactDelete(TransactRead):
    pass
