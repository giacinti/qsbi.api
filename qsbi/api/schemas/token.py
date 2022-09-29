from datetime import datetime, timedelta
from typing import Union, List, Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    login: Optional[str] = None
    scopes: List[str] = []
    exp: Union[datetime, timedelta, None]

