from typing import Any
from pydantic import BaseModel, root_validator

# convenient functions
def is_null(v) -> bool:  # type: ignore
    """ v is None or for a list or a tuple, at least one element is null 
Eg: ('a','b') is not null, ('a',None) is null
    ('a',('b','c')) is not null, ('a',('b',None)) is null """
    if isinstance(v,list) or isinstance(v,tuple):
        for x in v:
            if is_null(x):
                return True
    else:
        return v is None
    
def mapget(dic,key) -> Any:
    # special case for strings
    if isinstance(key,str):
        return dic.get(key)
    try:
        return tuple(map(lambda x: mapget(dic,x),key))
    except TypeError: # key is not an iterable
        return dic.get(key)

# custom validators
def check_all_non_null(values,*fields)-> Any:
    if not fields:
        fields=list(values.keys())
    for f in fields:
        if is_null(values.get(f)):
            raise ValueError(f"field {f} cannot be null")
    return values

def check_one_non_null(values,*fields) -> Any:
    if not fields:
        fields=list(values.keys())
    if all(map(lambda x: is_null(mapget(values,x)),fields)):
        raise ValueError(f"at least one field from {fields} should not be null")
    return values

##############################################################################
class BaseORM(BaseModel):
    class Config:
        orm_mode = True

# basic class - change here to skip ORM
class BaseQsbi(BaseORM):
    pass

class BaseAny(BaseQsbi):
    @root_validator
    def BaseAny_validate(cls, values) -> Any:
        return check_one_non_null(values)

class BaseId(BaseQsbi):
    @root_validator
    def BaseId_validate(cls, values) -> Any:
        return check_all_non_null(values,'id')
    
class BaseIdOrName(BaseQsbi):
    @root_validator
    def BaseIdOrName_validate(cls, values) -> Any:
        return check_one_non_null(values,'id','name')


class BaseIdOrAccount(BaseQsbi):
    @root_validator
    def BaseIdOrAccount_validate(cls, values) -> Any:
        return check_one_non_null(values,'id',('name','account'))

