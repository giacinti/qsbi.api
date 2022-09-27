from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.user
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.user.User)
def create_user(
        *,
        user_in: qsbi.api.schemas.user.UserCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.user.User:
    """
    create a new user
    """
    user = qsbi.crud.user.create(sess, user_in)
    return user

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.user.UserSeq)
def list_users(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.user.UserSeq:
    """
    list all users
    """
    users = qsbi.crud.user.list(sess, skip, limit)
    return {"results": users}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.user.UserSeq)
def search_users(
        *,
        user_in: qsbi.api.schemas.user.UserRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.user.UserSeq:
    """
    search users
    """
    users = qsbi.crud.user.search(sess, user_in, limit)
    return {"results": users}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.user.User)
def get_user_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.user.User]:
    """
    get user by id
    """
    result = qsbi.crud.user.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with id {id} not found"
        )
    return result
  
@router.get("/login/{login}", status_code=200, response_model=qsbi.api.schemas.user.User)
def get_user_by_login(
        *,
        login: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.user.User]:
    """
    get user by login
    """
    result = qsbi.crud.user.get_by(sess, 'login', login)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.user.User)
def update_user(
        *,
        user_in: qsbi.api.schemas.user.UserUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.user.User]:
    """
    update existing user
    """
    result = qsbi.crud.user.update(sess, user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.user.UserDict)
def delete_user(
        *,
        user_in: qsbi.api.schemas.user.UserDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one user
    """
    result = qsbi.crud.user.delete(sess, user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result
