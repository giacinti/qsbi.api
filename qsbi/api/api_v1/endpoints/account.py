from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.account as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.Account)
async def create_account(
        *,
        account_in: schema.AccountCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Account:
    """
    create a new account
    """
    account: schema.Account  = await crud.account.create(account_in)
    return account

## READ
@router.get("/list", status_code=200, response_model=List[schema.Account])
async def list_accounts(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Account]:
    """
    list all accounts
    """
    accounts: List[schema.Account] = await crud.account.list(skip, limit)
    return accounts

@router.post("/search", status_code=200, response_model=List[schema.Account])
async def search_accounts(
        *,
        account_in: schema.Account,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Account]:
    """
    search accounts
    """
    accounts: List[schema.Account] = await crud.account.search(account_in, limit)
    return accounts

@router.get("/id/{id}", status_code=200, response_model=schema.Account)
async def get_account_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Account]:
    """
    get account by id
    """
    result: Optional[schema.Account] = await crud.account.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Account)
async def get_account_by_name(
        *,
        name: str,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Account]:
    """
    get account by name
    """
    result: Optional[schema.Account] = await crud.account.get_by('name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with name {name} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_accounts(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all accounts
    """
    count: int = await crud.account.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.Account)
async def update_account(
        *,
        account_in: schema.AccountUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Account]:
    """
    update existing account
    """
    result: Optional[schema.Account] = await crud.account.update(account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.Account)
async def delete_account(
        *,
        account_in: schema.AccountDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.Account]:
    """
    delete one account
    """
    result: Optional[schema.Account] = await crud.account.delete(account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result