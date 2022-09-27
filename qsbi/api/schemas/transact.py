from datetime import datetime
from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_one_non_null, check_all_non_null
from .account import Account
from .party import Party
from .category import Category
from .sub_category import SubCategory
from .currency import Currency
from .payment import Payment
from .audit_log import AuditLog
from .reconcile import Reconcile

class Transact(BaseQsbi):
    id : Optional[int]
    account_id : Optional[int]
    transaction_date : Optional[datetime]
    value_date : Optional[datetime]
    party_id : Optional[int]
    category_id : Optional[int]
    sub_category_id : Optional[int]
    notes : Optional[str]
    amount : Optional[float]
    currency_id : Optional[int]
    exchange_rate : Optional[float]
    exchange_fees : Optional[float]
    payment_id : Optional[int]
    master_id : Optional[int]
    reconcile_id : Optional[int]
    log_id : Optional[int]

class TransactDict(BaseModel):
    id : Optional[int]
    account_id : Optional[int]
    transaction_date : Optional[datetime]
    value_date : Optional[datetime]
    party_id : Optional[int]
    category_id : Optional[int]
    sub_category_id : Optional[int]
    notes : Optional[str]
    amount : Optional[float]
    currency_id : Optional[int]
    exchange_rate : Optional[float]
    exchange_fees : Optional[float]
    payment_id : Optional[int]
    master_id : Optional[int]
    reconcile_id : Optional[int]
    log_id : Optional[int]

class TransactCreate(Transact):
    @root_validator
    def TransactCreate_validate(cls, values):
        return check_all_non_null(values,'account','log')
    pass

class TransactRead(Transact,BaseAny):
    pass

class TransactUpdate(Transact,BaseId):
    pass

class TransactDelete(BaseId):
    id : Optional[int]
        
class TransactSeq(BaseModel):
    results: Sequence[Transact]
