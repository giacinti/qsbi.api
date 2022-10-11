from datetime import datetime, timedelta
from typing import Union, List, Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserToken(BaseModel):
    login: Optional[str] = None
    exp: Union[datetime, timedelta, None]


class TokenData(UserToken):
    scopes: List[str] = []
