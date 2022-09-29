from datetime import timedelta
from typing import Optional
from fastapi import APIRouter, Security, Query

import qsbi.api.security.auth as auth
import qsbi.api.security.deps as deps
import qsbi.api.schemas.token as schema

router = APIRouter()

@router.post("/create", status_code=201, response_model=schema.Token)
async def create_access_token(
        *,
        token_data: schema.TokenData,
        curr_user = Security(deps.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.Token]:
    """
    create an access token
    """
    access_token = auth.create_access_token(
        data={"sub": token_data.login, "scopes": token_data.scopes},
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
