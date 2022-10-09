from typing import Any, Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null

class Category(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    type_id: Optional[int]

class CategoryCreate(Category):
    @root_validator
    def CategoryCreate_validate(cls, values) -> Any:
        return check_all_non_null(values,'name')

class CategoryRead(BaseAny):
    id: Optional[int]
    name: Optional[str]

class CategoryUpdate(Category,BaseIdOrName):
    pass

class CategoryDelete(CategoryRead):
    pass

