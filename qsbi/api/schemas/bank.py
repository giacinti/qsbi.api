from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseORM, BaseAny, BaseIdOrName, check_one_non_null, check_all_non_null

class Bank(BaseORM):
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

class BankDict(BaseModel):
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
    def BankCreate_validate(cls, values):
        return check_all_non_null(values,'name')

class BankRead(Bank,BaseAny):
    pass

class BankUpdate(Bank,BaseIdOrName):
    pass

class BankDelete(BaseIdOrName):
    id: Optional[int]
    name: Optional[str]

        
class BankSeq(BaseModel):
    results: Sequence[Bank]

