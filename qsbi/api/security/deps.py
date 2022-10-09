from typing import Optional
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError
from pydantic import ValidationError

import qsbi.api.crud as crud
import qsbi.api.schemas.user as user_schema
import qsbi.api.schemas.token as token_schema
import qsbi.api.security.auth as auth
from qsbi.api.config import settings as settings

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/token",
    # scopes={"login": "Minimal scope for accessing API",
    #         "create": "Create authorization.",
    #         "read": "Read authorization.",
    #         "update": "Update authorization.",
    #         "delete": "Delete authorization.",
    #         "admin": "Super user authorization."},
)

async def get_current_user(
        security_scopes: SecurityScopes,
        token: str = Depends(oauth2_scheme),
	) -> Optional[user_schema.User]:
    if security_scopes.scopes:
        authenticate_value: str = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        token_data: Optional[token_schema.TokenData] = auth.decode_access_token(token)
    except (JWTError, ValidationError):
        raise credentials_exception
    if not token_data:
        raise credentials_exception
    user: Optional[User] = await auth.get_user(user_schema.User(login=token_data.login))  # type: ignore
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        #import pdb; pdb.set_trace()
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
        current_user: user_schema.User = Security(get_current_user, scopes=["login"])
	) -> Optional[user_schema.User]:
    if not current_user.active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"user account {current_user.login} is deactivated")
    return current_user


