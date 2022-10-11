# authentication (password & token) and authorization (token scope)
from datetime import datetime, timedelta
from typing import Any, List, Optional, Union

from passlib.context import CryptContext
from jose import jwt

import qsbi.api.crud as crud
import qsbi.api.config as config

from qsbi.api.schemas.user import User, UserRead
from qsbi.api.schemas.token import TokenData


pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user(user_in: UserRead) -> Optional[User]:
    obj: Optional[User] = None
    obj_list: List[User] = await crud.user.search(user_in, 1)  # type: ignore
    try:
        obj = obj_list[0]
    except IndexError:
        obj = None
    return obj


def get_password_hash(password: Optional[str]) -> Optional[str]:
    hash = None
    if password:
        hash = pwd_context.hash(password)
    return hash


def verify_password(plain_password: str, hashed_password: Optional[str]) -> bool:
    if not hashed_password:
        return False
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(user_in: UserRead,
                            password: str,
                            ) -> Optional[User]:
    user: Optional[User] = await get_user(user_in)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_access_token(data: dict,
                        expiration: Union[datetime, timedelta, None] = None
                        ) -> str:
    to_encode: dict = data.copy()
    if expiration:
        if isinstance(expiration, datetime):
            expire: datetime = expiration
        elif isinstance(expiration, timedelta):
            expire = datetime.utcnow() + expiration
        else:  # should not be there
            raise ValueError("wrong data type for expiration")
    else:
        expire = datetime.utcnow() + timedelta(minutes=config.settings.QSBI_JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode,
                                  config.settings.QSBI_JWT_SECRET_KEY,  # type: ignore
                                  algorithm=config.settings.QSBI_JWT_ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[TokenData]:
    token_data: Optional[TokenData] = None
    payload: dict[str, Any] = jwt.decode(token,
                                         config.settings.QSBI_JWT_SECRET_KEY,  # type: ignore
                                         algorithms=[config.settings.QSBI_JWT_ALGORITHM])
    login: Optional[str] = payload.get("sub")
    if login is not None:
        token_scopes: List = payload.get("scopes", [])
        exp: datetime = datetime.fromtimestamp(payload.get("exp", 0))
        token_data = TokenData(scopes=token_scopes, login=login, exp=exp)
    return token_data
