from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_one_non_null, check_all_non_null

class PaymentType(BaseQsbi):
    id: Optional[int]
    name: Optional[str]

class PaymentTypeDict(BaseModel):
    id: Optional[int]
    name: Optional[str]

class PaymentTypeCreate(PaymentType):
    @root_validator
    def PaymentTypeCreate_validate(cls, values):
        return check_all_non_null(values,'name')

class PaymentTypeRead(PaymentType,BaseAny):
    pass

class PaymentTypeUpdate(PaymentType,BaseIdOrName):
    pass

class PaymentTypeDelete(BaseIdOrName):
    id: Optional[int]
    name: Optional[str]
        
class PaymentTypeSeq(BaseModel):
    results: Sequence[PaymentType]
