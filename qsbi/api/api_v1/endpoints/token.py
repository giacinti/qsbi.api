from typing import Optional, Dict
from fastapi import APIRouter, Query, HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordRequestForm


import qsbi.api.security.auth as auth
import qsbi.api.schemas.token as schema
import qsbi.api.schemas.user as user_schema
import qsbi.api.crud as crud


router = APIRouter()
@router.post("", response_model=schema.Token)
async def login_for_access_token(
        *,
        form_data: OAuth2PasswordRequestForm = Depends(),
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> dict:
    user_in = user_schema.User(login=form_data.username)
    user = await auth.authenticate_user(sess, user_in, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(
        data={"sub": user.login, "scopes": form_data.scopes},
    )
    return {"access_token": access_token, "token_type": "bearer"}
