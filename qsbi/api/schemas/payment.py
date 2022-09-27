from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrAccount, BaseId, check_one_non_null, check_all_non_null
from .account import Account
from .payment_type import PaymentType

class Payment(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    account_id: Optional[int]
    current: Optional[int]
    type_id: Optional[int]

class PaymentDict(BaseModel):
    id: Optional[int]
    name: Optional[str]
    account_id: Optional[int]
    current: Optional[int]
    type_id: Optional[int]

class PaymentCreate(Payment):
    @root_validator
    def PaymentCreate_validate(cls, values):
        return check_all_non_null(values,'name','account')

class PaymentRead(Payment,BaseAny):
    pass

class PaymentUpdate(Payment,BaseIdOrAccount):
    pass

class PaymentDelete(BaseId):
    id: Optional[int]

class PaymentSeq(BaseModel):
    results: Sequence[Payment]

