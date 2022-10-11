from typing import Any, Optional, List
from pydantic import root_validator

from .base import BaseQsbi, BaseAny, check_one_non_null, check_all_non_null


class User(BaseQsbi):
    id: Optional[int]
    login: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    active: Optional[bool] = False
    notes: Optional[str]
    password: Optional[str]
    scopes: Optional[List[str]] = []


class UserCreate(User):
    @root_validator
    def UserCreate_validate(cls, values) -> Any:
        return check_all_non_null(values, 'login', 'password')


class UserRead(BaseAny):
    id: Optional[int]
    login: Optional[str]


class UserUpdate(User):
    @root_validator
    def UserValid_validate(cls, values) -> Any:
        return check_one_non_null(values, 'id', 'login')


class UserDelete(UserRead):
    pass
