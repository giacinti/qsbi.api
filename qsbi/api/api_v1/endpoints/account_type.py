from fastapi import APIRouter, HTTPException, Security
from typing import Optional, List

import qsbi.api.schemas.account_type as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()


@router.post("", status_code=201, response_model=schema.AccountType)
async def create_account_type(
        *,
        account_type_in: schema.AccountTypeCreate,
        curr_user=Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.AccountType:
    """
    create a new account_type
    """
    account_type: schema.AccountType = await crud.account_type.create(account_type_in)
    return account_type


@router.get("/list", status_code=200, response_model=List[schema.AccountType])
async def list_account_types(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.AccountType]:
    """
    list all account_types
    """
    account_types: List[schema.AccountType] = await crud.account_type.list(skip, limit)
    return account_types


@router.post("/search", status_code=200, response_model=List[schema.AccountType])
async def search_account_types(
        *,
        account_type_in: schema.AccountType,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.AccountType]:
    """
    search account_types
    """
    account_types: List[schema.AccountType] = await crud.account_type.search(account_type_in, limit)
    return account_types


@router.get("/id/{id}", status_code=200, response_model=schema.AccountType)
async def get_account_type_by_id(
        *,
        id: int,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.AccountType]:
    """
    get account_type by id
    """
    result: Optional[schema.AccountType] = await crud.account_type.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType with id {id} not found"
        )
    return result


@router.get("/name/{name}", status_code=200, response_model=schema.AccountType)
async def get_account_type_by_name(
        *,
        name: str,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.AccountType]:
    """
    get account_type by name
    """
    result: Optional[schema.AccountType] = await crud.account_type.get_by('name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType with name {name} not found"
        )
    return result


@router.get("/count", status_code=200, response_model=int)
async def count_account_types(
        *,
        curr_user=Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all account_types
    """
    count: int = await crud.account_type.count()
    return count


@router.put("", status_code=201, response_model=schema.AccountType)
async def update_account_type(
        *,
        account_type_in: schema.AccountTypeUpdate,
        curr_user=Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.AccountType]:
    """
    update existing account_type
    """
    result: Optional[schema.AccountType] = await crud.account_type.update(account_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType {account_type_in} not found"
        )
    return result


@router.delete("", status_code=200, response_model=schema.AccountType)
async def delete_account_type(
        *,
        account_type_in: schema.AccountTypeDelete,
        curr_user=Security(auth.get_current_active_user, scopes=["delete"]),
        ) -> Optional[schema.AccountType]:
    """
    delete one account_type
    """
    result: Optional[schema.AccountType] = await crud.account_type.delete(account_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType {account_type_in} not found"
        )
    return result
