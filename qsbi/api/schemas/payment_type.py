from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null


class PaymentType(BaseQsbi):
    id: Optional[int]
    name: Optional[str]


class PaymentTypeCreate(PaymentType):
    @root_validator
    def PaymentTypeCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'name')


class PaymentTypeRead(BaseAny):
    id: Optional[int]
    name: Optional[str]


class PaymentTypeUpdate(PaymentType, BaseIdOrName):
    pass


class PaymentTypeDelete(PaymentTypeRead):
    pass
