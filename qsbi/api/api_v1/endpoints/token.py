from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm


import qsbi.api.security.auth as auth
import qsbi.api.schemas.token as schema
import qsbi.api.schemas.user as user_schema


router = APIRouter()
@router.post("", response_model=schema.Token)
async def login_for_access_token(
        *,
        form_data: OAuth2PasswordRequestForm = Depends(),
	) -> dict:
    user_in: user_schema.UserRead = user_schema.UserRead(login=form_data.username)  # type: ignore
    user: Optional[user_schema.User] = await auth.authenticate_user(user_in, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(
        data={"sub": user.login, "scopes": user.scopes},
    )
    return {"access_token": access_token, "token_type": "bearer"}
