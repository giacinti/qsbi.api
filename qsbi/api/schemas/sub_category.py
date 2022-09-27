from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_one_non_null, check_all_non_null
from .category import Category

class SubCategory(BaseQsbi):
    id : Optional[int]
    name : Optional[str]
    category_id: Optional[int]

    @root_validator
    def SubCategory_validate(cls, values):
        return check_one_non_null(values,'id',('name','category'))

class SubCategoryDict(BaseModel):
    id : Optional[int]
    name : Optional[str]
    category_id: Optional[int]

class SubCategoryCreate(SubCategory):
    @root_validator
    def SubCategoryCreate_validate(cls, values):
        return check_all_non_null(values,'name','category')

class SubCategoryRead(SubCategory,BaseAny):
    pass

class SubCategoryUpdate(SubCategory,BaseId):
    pass

class SubCategoryDelete(BaseId):
    id : Optional[int]
        
class SubCategorySeq(BaseModel):
    results: Sequence[SubCategory]

