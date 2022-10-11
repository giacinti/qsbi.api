from typing import Any, Optional
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_one_non_null, check_all_non_null


class SubCategory(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    category_id: Optional[int]

    @root_validator
    def SubCategory_validate(cls, values) -> Any:
        return check_one_non_null(values, 'id', ('name', 'category'))


class SubCategoryCreate(SubCategory):
    @root_validator
    def SubCategoryCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'name', 'category')


class SubCategoryRead(BaseAny):
    id: int


class SubCategoryUpdate(SubCategory, BaseId):
    pass


class SubCategoryDelete(SubCategoryRead):
    pass
