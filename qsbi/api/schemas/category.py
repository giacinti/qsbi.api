from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_one_non_null, check_all_non_null
from .category_type import CategoryType

class Category(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    type_id: Optional[int]

class CategoryDict(BaseModel):
    id: Optional[int]
    name: Optional[str]
    type_id: Optional[int]


class CategoryCreate(Category):
    @root_validator
    def CategoryCreate_validate(cls, values):
        return check_all_non_null(values,'name')

class CategoryRead(Category,BaseAny):
    pass

class CategoryUpdate(Category,BaseIdOrName):
    pass

class CategoryDelete(BaseIdOrName):
    id: Optional[int]
    name: Optional[str]
        
class CategorySeq(BaseModel):
    results: Sequence[Category]

