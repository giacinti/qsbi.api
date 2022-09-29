from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.user as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth
import qsbi.api.security.auth as pwd

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.User)
async def create_user(
        *,
        user_in: schema.User,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> schema.User:
    """
    create a new user
    """
    user_in.password = pwd.get_password_hash(user_in.password)
    user = await crud.user.create(sess, user_in)
    return user

## READ
@router.get("/list", status_code=200, response_model=schema.UserSeq)
async def list_users(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> schema.UserSeq:
    """
    list all users
    """
    users = await crud.user.list(sess, skip, limit)
    return {"results": users}

@router.post("/search", status_code=200, response_model=schema.UserSeq)
async def search_users(
        *,
        user_in: schema.UserRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> schema.UserSeq:
    """
    search users
    """
    users = await crud.user.search(sess, user_in, limit)
    return {"results": users}

@router.get("/id/{id}", status_code=200, response_model=schema.User)
async def get_user_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.User]:
    """
    get user by id
    """
    result = await crud.user.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with id {id} not found"
        )
    return result
  
@router.get("/login/{login}", status_code=200, response_model=schema.User)
async def get_user_by_login(
        *,
        login: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.User]:
    """
    get user by login
    """
    result = await crud.user.get_by(sess, 'login', login)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_users(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all users
    """
    count = await crud.user.count(sess)
    return {"count": count}

## UPDATE
@router.put("", status_code=201, response_model=schema.User)
async def update_user(
        *,
        user_in: schema.User,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.User]:
    """
    update existing user
    """
    result = await crud.user.update(sess, user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.UserDict)
async def delete_user(
        *,
        user_in: schema.UserDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["admin"]),
	) -> Optional[Dict]:
    """
    delete one user
    """
    result = await crud.user.delete(sess, user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result
