from datetime import datetime
from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseORM, BaseAny, BaseId, check_one_non_null, check_all_non_null
from .account import Account
from .party import Party
from .category import Category
from .sub_category import SubCategory
from .currency import Currency
from .payment import Payment
from .audit_log import AuditLog

class Scheduled(BaseORM):
    id : Optional[int]
    account : Optional[Account]
    start_date : Optional[datetime]
    limit_date : Optional[datetime]
    frequency : Optional[int]
    automatic : Optional[bool] = False
    party : Optional[Party]
    category : Optional[Category]
    sub_category : Optional[SubCategory]
    notes : Optional[str]
    amount : Optional[float]
    currency : Optional[Currency]
    payment : Optional[Payment]
    splitted : Optional[bool] = False
    master : Optional['Scheduled']
    log : Optional[AuditLog]

    @root_validator
    def Scheduled_validate(cls,values):
        if values.get('splitted') == True:
            if values.get('master') is None:
                raise ValueError("master is needed if splitted is set to True")
        return values

class ScheduledDict(BaseModel):
    id : Optional[int]
    account_id : Optional[int]
    start_date : Optional[datetime]
    limit_date : Optional[datetime]
    frequency : Optional[int]
    automatic : Optional[bool]
    party_id : Optional[int]
    category_id : Optional[int]
    sub_category_id : Optional[int]
    notes : Optional[str]
    amount : Optional[float]
    currency_id : Optional[int]
    payment_id : Optional[int]
    splitted : Optional[bool]
    master_id : Optional[int]
    log_id : Optional[int]

class ScheduledCreate(Scheduled):
    @root_validator
    def ScheduledCreate_validate(cls, values):
        return check_all_non_null(values,'account','log')

class ScheduledRead(Scheduled,BaseAny):
    pass

class ScheduledUpdate(Scheduled,BaseId):
    pass

class ScheduledDelete(BaseId):
    id : Optional[int]
        
class ScheduledSeq(BaseModel):
    results: Sequence[Scheduled]

