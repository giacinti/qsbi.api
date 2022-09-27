from datetime import datetime
from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrAccount, BaseId, check_one_non_null, check_all_non_null
from .account import Account
from .audit_log import AuditLog

class Reconcile(BaseQsbi):
    id : Optional[int]
    name : Optional[str]
    account_id : Optional[int]
    start_date : Optional[datetime]
    end_date : Optional[datetime]
    start_balance : Optional[float]
    end_balance : Optional[float]
    log_id : Optional[int]

class ReconcileDict(BaseModel):
    id : Optional[int]
    name : Optional[str]
    account_id : Optional[int]
    start_date : Optional[datetime]
    end_date : Optional[datetime]
    start_balance : Optional[float]
    end_balance : Optional[float]
    log_id : Optional[int]


class ReconcileCreate(Reconcile):
    @root_validator
    def ReconcileCreate_validate(cls, values):
        return check_all_non_null(values,'name','account','log')

class ReconcileRead(Reconcile,BaseAny):
    pass

class ReconcileUpdate(Reconcile,BaseIdOrAccount):
    pass

class ReconcileDelete(BaseId):
    id : Optional[int]
        
class ReconcileSeq(BaseModel):
    results: Sequence[Reconcile]

