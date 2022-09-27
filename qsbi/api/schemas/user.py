from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseORM, BaseAny, check_one_non_null, check_all_non_null

##############################################################################
class User(BaseORM):
    id : Optional[int]
    login: Optional[str]
    firstname : Optional[str]
    lastname : Optional[str]
    notes : Optional[str]

class UserValid(BaseModel):
    @root_validator
    def UserValid_validate(cls, values):
        return check_one_non_null(values,'id','login')

class UserDict(BaseModel):
    id : Optional[int]
    login: Optional[str]
    firstname : Optional[str]
    lastname : Optional[str]
    notes : Optional[str]

class UserCreate(User):
    @root_validator
    def UserCreate_validate(cls, values):
        return check_all_non_null(values,'login')

class UserRead(User,BaseAny):
    pass

class UserUpdate(User,UserValid):
    pass

class UserDelete(UserValid):
    id : Optional[int]
    login: Optional[str]

class UserSeq(BaseModel):
    results: Sequence[User]

        
