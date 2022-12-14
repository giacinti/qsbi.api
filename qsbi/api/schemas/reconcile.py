from datetime import datetime
from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrAccount, check_all_non_null


class Reconcile(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    account_id: Optional[int]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    start_balance: Optional[float]
    end_balance: Optional[float]
    log_id: Optional[int]


class ReconcileCreate(Reconcile):
    @root_validator
    def ReconcileCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'name', 'account', 'log')


class ReconcileRead(BaseAny):
    id: int


class ReconcileUpdate(Reconcile, BaseIdOrAccount):
    pass


class ReconcileDelete(ReconcileRead):
    pass
