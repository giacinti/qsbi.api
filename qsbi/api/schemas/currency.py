from typing import Optional, Sequence
from pydantic import BaseModel,root_validator

from .base import BaseQsbi, BaseAny, check_one_non_null, check_all_non_null

class Currency(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    nickname: Optional[str]
    code: Optional[str]

class CurrencyDict(BaseModel):
    id: Optional[int]
    name: Optional[str]
    nickname: Optional[str]
    code: Optional[str]

class CurrencyCreate(Currency):
    @root_validator
    def CurrencyCreate_validate(cls, values):
        return check_all_non_null(values,'name','nickname','code')

class CurrencyRead(Currency,BaseAny):
    pass

class CurrencyUpdate(Currency,BaseAny):
    pass

class CurrencyDelete(BaseAny):
    id: Optional[int]
    name: Optional[str]
    nickname: Optional[str]
    code: Optional[str]

class CurrencySeq(BaseModel):
    results: Sequence[Currency]
