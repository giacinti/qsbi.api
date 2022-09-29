from datetime import timedelta
from typing import Optional
from fastapi import APIRouter, Security, Depends, Query

import qsbi.api.security.auth as auth
import qsbi.api.security.deps as deps
import qsbi.api.schemas.token as schema
import qsbi.api.schemas.user as user_schema
import qsbi.api.crud as crud

router = APIRouter()

@router.post("/create", status_code=201, response_model=schema.Token)
async def create_access_token(
        *,
        token_data: schema.UserToken,
        curr_user = Security(deps.get_current_active_user, scopes=["admin"]),
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Token]:
    """
    create an access token
    """
    user_in = user_schema.User(login=token_data.login)
    user = await auth.get_user(sess, user_in)
    if not user:
        raise HTTPException(status_code=400, detail=f"Unknown user {token_data.login}")
    access_token = auth.create_access_token(
        data={"sub": token_data.login, "scopes": user.scopes},
        expiration=token_data.exp,
    )
    return schema.Token(access_token=access_token, token_type="bearer")
    
@router.get("/decode", status_code=200, response_model=schema.TokenData)
async def decode_access_token(
        *,
        token: str,
        curr_user = Security(deps.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.TokenData]:
    """
    decode an access token
    """
    return auth.decode_access_token(token)
