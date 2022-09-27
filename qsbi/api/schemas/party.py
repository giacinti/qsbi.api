from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseORM, BaseAny, BaseIdOrName, check_one_non_null, check_all_non_null

class Party(BaseORM):
    id: Optional[int]
    name: Optional[str]
    desc: Optional[str]

class PartyDict(BaseModel):
    id: Optional[int]
    name: Optional[str]
    desc: Optional[str]

class PartyCreate(Party):
    @root_validator
    def PartyCreate_validate(cls, values):
        return check_all_non_null(values,'name')

class PartyRead(Party,BaseAny):
    pass

class PartyUpdate(Party,BaseIdOrName):
    pass

class PartyDelete(BaseIdOrName):
    id: Optional[int]
    name: Optional[str]
        
class PartySeq(BaseModel):
    results: Sequence[Party]

