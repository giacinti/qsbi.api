from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseORM, BaseAny, BaseIdOrName, check_one_non_null, check_all_non_null

class CategoryType(BaseORM):
    id: Optional[int]
    name: Optional[str]

class CategoryTypeDict(BaseModel):
    id: Optional[int]
    name: Optional[str]

class CategoryTypeCreate(CategoryType):
    @root_validator
    def CategoryTypeCreate_validate(cls, values):
        return check_all_non_null(values,'name')

class CategoryTypeRead(CategoryType,BaseAny):
    pass

class CategoryTypeUpdate(CategoryType,BaseIdOrName):
    pass

class CategoryTypeDelete(BaseIdOrName):
    id: Optional[int]
    name: Optional[str]

class CategoryTypeSeq(BaseModel):
    results: Sequence[CategoryType]
