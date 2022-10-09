from typing import Any, Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null

class CategoryType(BaseQsbi):
    id: Optional[int]
    name: Optional[str]

class CategoryTypeCreate(CategoryType):
    @root_validator
    def CategoryTypeCreate_validate(cls, values) -> Any:
        return check_all_non_null(values,'name')

class CategoryTypeRead(BaseAny):
    id: Optional[int]
    name: Optional[str]

class CategoryTypeUpdate(CategoryType,BaseIdOrName):
    pass

class CategoryTypeDelete(CategoryTypeRead):
    pass
