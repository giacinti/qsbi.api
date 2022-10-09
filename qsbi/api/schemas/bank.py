from typing import Any, Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null

class Bank(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    code : Optional[int]
    bic : Optional[str]
    address : Optional[str]
    tel : Optional[str]
    mail : Optional[str]
    web : Optional[str]
    contact_name : Optional[str]
    contact_fax : Optional[str]
    contact_tel : Optional[str]
    contact_mail : Optional[str]
    notes : Optional[str]

class BankCreate(Bank):
    @root_validator
    def BankCreate_validate(cls, values) -> Any:
        return check_all_non_null(values,'name')

class BankRead(BaseAny):
    id: Optional[int]
    name: Optional[str]

class BankUpdate(Bank,BaseIdOrName):
    pass

class BankDelete(BankRead):
    pass

