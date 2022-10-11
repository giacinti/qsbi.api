from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrAccount, check_all_non_null


class Payment(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    account_id: Optional[int]
    current: Optional[int]
    type_id: Optional[int]


class PaymentCreate(Payment):
    @root_validator
    def PaymentCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'name', 'account')


class PaymentRead(BaseAny):
    id: int


class PaymentUpdate(Payment, BaseIdOrAccount):
    pass


class PaymentDelete(PaymentRead):
    pass
