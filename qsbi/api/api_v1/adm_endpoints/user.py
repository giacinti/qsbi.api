from fastapi import APIRouter, HTTPException, Security
from typing import List, Optional

import qsbi.api.schemas.user as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth
import qsbi.api.security.auth as pwd

router = APIRouter()


@router.post("", status_code=201, response_model=schema.User)
async def create_user(
        *,
        user_in: schema.UserCreate,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> schema.User:
    """
    create a new user
    """
    user_in.password = pwd.get_password_hash(user_in.password)
    user: schema.User = await crud.user.create(user_in)
    return user


@router.get("/list", status_code=200, response_model=List[schema.User])
async def list_users(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> List[schema.User]:
    """
    list all users
    """
    users: List[schema.User] = await crud.user.list(skip, limit)
    return users


@router.post("/search", status_code=200, response_model=List[schema.User])
async def search_users(
        *,
        user_in: schema.User,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> List[schema.User]:
    """
    search users
    """
    users: List[schema.User] = await crud.user.search(user_in, limit)
    return users


@router.get("/id/{id}", status_code=200, response_model=schema.User)
async def get_user_by_id(
        *,
        id: int,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.User]:
    """
    get user by id
    """
    result: schema.User = await crud.user.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with id {id} not found"
        )
    return result


@router.get("/login/{login}", status_code=200, response_model=schema.User)
async def get_user_by_login(
        *,
        login: str,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.User]:
    """
    get user by login
    """
    result: schema.User = await crud.user.get_by('login', login)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    return result


@router.get("/count", status_code=200, response_model=int)
async def count_users(
        *,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> int:
    """
    count all users
    """
    count: int = await crud.user.count()
    return count


@router.put("", status_code=201, response_model=schema.User)
async def update_user(
        *,
        user_in: schema.User,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.User]:
    """
    update existing user
    """
    result: schema.User = await crud.user.update(user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result


@router.delete("", status_code=200, response_model=Optional[schema.User])
async def delete_user(
        *,
        user_in: schema.UserDelete,
        curr_user=Security(auth.get_current_active_user, scopes=["admin"]),
        ) -> Optional[schema.User]:
    """
    delete one user
    """
    result: Optional[schema.User] = await crud.user.delete(user_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {user_in} not found"
        )
    return result
