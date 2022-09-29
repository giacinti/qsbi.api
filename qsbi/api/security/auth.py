# authentication (password & token) and authorization (token scope)
from datetime import datetime, timedelta
from typing import Optional, Union
from pydantic import ValidationError

from passlib.context import CryptContext
from jose import jwt

import qsbi.api.schemas.user as user_schema
import qsbi.api.schemas.token as token_schema
import qsbi.api.crud as crud
import qsbi.api.config as config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

##############################################################################
#
async def get_user(sess: crud.CRUDSession,
                   user_in: user_schema.User,
                   )-> Optional[user_schema.User]:
    obj = None
    obj_list = await crud.user.search(sess, user_in, 1)
    try:
        obj = obj_list[0]
    except IndexError:
        obj = None
    return obj


##############################################################################
# password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def authenticate_user(sess: crud.CRUDSession,
                            user_in: user_schema.User,
                            password: str,
                            ) -> Union[bool,user_schema.User]:
    user = await get_user(sess, user_in)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

##############################################################################
# token
def create_access_token(data: dict,
                        expiration: Union[datetime, timedelta, None] = None
                        ) -> str:
    to_encode = data.copy()
    if expiration:
        if isinstance(expiration, datetime):
            expire = expiration
        elif isinstance(expiration, timedelta):
            expire = datetime.utcnow() + expiration
        else: # should not be there
            raise ValueError("wrong data type for expiration")
    else:
        expire = datetime.utcnow() + timedelta(minutes=config.settings.QSBI_JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             config.settings.QSBI_JWT_SECRET_KEY,
                             algorithm=config.settings.QSBI_JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Optional[token_schema.TokenData]:
    token_data = None
    payload = jwt.decode(token,
                         config.settings.QSBI_JWT_SECRET_KEY,
                         algorithms=[config.settings.QSBI_JWT_ALGORITHM])
    login: str = payload.get("sub")
    if login is not None:
        token_scopes = payload.get("scopes", [])
        exp = datetime.fromtimestamp(payload.get("exp"))
        token_data = token_schema.TokenData(scopes=token_scopes, login=login, exp=exp)
    return token_data
