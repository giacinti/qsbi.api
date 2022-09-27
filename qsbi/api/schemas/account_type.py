from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null

class AccountType(BaseQsbi):
    id: Optional[int]
    name: Optional[str]

class AccountTypeDict(BaseModel):
    id: Optional[int]
    name: Optional[str]
    
class AccountTypeCreate(AccountType):
    @root_validator
    def AccountTypeCreate_validate(cls, values):
        return check_all_non_null(values,'name')

class AccountTypeRead(AccountType,BaseAny):
    pass

class AccountTypeUpdate(AccountType,BaseIdOrName):
    pass

class AccountTypeDelete(BaseIdOrName):
    id: Optional[int]
    name: Optional[str]


class AccountTypeSeq(BaseModel):
    results: Sequence[AccountType]

