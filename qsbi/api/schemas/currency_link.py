from datetime import datetime
from typing import Optional, Sequence
from pydantic import BaseModel,root_validator

from .base import BaseORM, BaseAny, BaseId, check_one_non_null, check_all_non_null
from .currency import Currency
from .audit_log import AuditLog

class CurrencyLink(BaseORM):
    id : Optional[int]
    cur1 : Optional[Currency]
    cur2 : Optional[Currency]
    rate : Optional[float]
    date : Optional[datetime]
    log :  Optional[AuditLog]

class CurrencyLinkDict(BaseModel):
    id : Optional[int]
    cur1_id : Optional[int]
    cur2_id : Optional[int]
    rate : Optional[float]
    date : Optional[datetime]
    log_id :  Optional[int]

class CurrencyLinkCreate(CurrencyLink):
    @root_validator
    def CurrencyLinkCreate_validate(cls, values):
        return check_all_non_null(values,'cur1','cur2','log')

class CurrencyLinkRead(CurrencyLink,BaseAny):
    pass

class CurrencyLinkUpdate(CurrencyLink,BaseId):
    pass

class CurrencyLinkDelete(BaseId):
    id : Optional[int]
    
class CurrencyLinkSeq(BaseModel):
    results: Sequence[CurrencyLink]


