from typing import Optional
from fastapi import APIRouter, HTTPException, Security

import qsbi.api.security.auth as auth
import qsbi.api.security.deps as deps

from qsbi.api.schemas.token import Token, UserToken, TokenData
from qsbi.api.schemas.user import User, UserRead


router = APIRouter()


@router.post("/create", status_code=201, response_model=Token)
async def create_access_token(
        *,
        token_data: UserToken,
        curr_user=Security(deps.get_current_active_user, scopes=["admin"]),
        ) -> Optional[Token]:
    """
    create an access token
    """
    user_in: UserRead = UserRead(login=token_data.login)  # type: ignore
    user: Optional[User] = await auth.get_user(user_in)
    if not user:
        raise HTTPException(status_code=400, detail=f"Unknown user {token_data.login}")
    access_token: str = auth.create_access_token(
        data={"sub": token_data.login, "scopes": user.scopes},
        expiration=token_data.exp,
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/decode", status_code=200, response_model=TokenData)
async def decode_access_token(
        *,
        token: str,
        curr_user=Security(deps.get_current_active_user, scopes=["admin"]),
        ) -> Optional[TokenData]:
    """
    decode an access token
    """
    return auth.decode_access_token(token)
