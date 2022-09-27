from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.user as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.User)
def create_user(
        *,
        user_in: schema.UserCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.User:
    """
    create a new user
    """
    user = crud.user.create(sess, user_in)
    return user

## READ
@router.get("/list", status_code=200, response_model=schema.UserSeq)
def list_users(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.UserSeq:
    """
    list all users
    """
    users = crud.user.list(sess, skip, limit)
    return {"results": users}

@router.post("/search", status_code=200, response_model=schema.UserSeq)
def search_users(
        *,
        user_in: schema.UserRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.UserSeq:
    """
    search users
    """
    users = crud.user.search(sess, user_in, limit)
    return {"results": users}

@router.get("/id/{id}", status_code=200, response_model=schema.User)
def get_user_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.User]:
    """
    get user by id
    """
    result = crud.user.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with id {id} not found"
        )
    return result
  
@router.get("/login/{login}", status_code=200, response_model=schema.User)
def get_user_by_login(
        *,
        login: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.User]:
    """
    get user by login
    """
    result = crud.user.get_by(sess, 'login', login)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.User)
def update_user(
        *,
        user_in: schema.UserUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.User]:
    """
    update existing user
    """
    result = crud.user.update(sess, user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.UserDict)
def delete_user(
        *,
        user_in: schema.UserDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one user
    """
    result = crud.user.delete(sess, user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result
