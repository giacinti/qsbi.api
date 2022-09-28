from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, Dict

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
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Account:
    """
    create a new account
    """
    account = await crud.account.create(sess, account_in)
    return account

## READ
@router.get("/list", status_code=200, response_model=schema.AccountSeq)
async def list_accounts(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.AccountSeq:
    """
    list all accounts
    """
    accounts = await crud.account.list(sess, skip, limit)
    return {"results": accounts}

@router.post("/search", status_code=200, response_model=schema.AccountSeq)
async def search_accounts(
        *,
        account_in: schema.AccountRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.AccountSeq:
    """
    search accounts
    """
    accounts = await crud.account.search(sess, account_in, limit)
    return {"results": accounts}

@router.get("/id/{id}", status_code=200, response_model=schema.Account)
async def get_account_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Account]:
    """
    get account by id
    """
    result = await crud.account.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Account)
async def get_account_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Account]:
    """
    get account by name
    """
    result = await crud.account.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with name {name} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_accounts(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all accounts
    """
    count = await crud.account.count(sess)
    return {"count": count}

## UPDATE
@router.put("", status_code=201, response_model=schema.Account)
async def update_account(
        *,
        account_in: schema.AccountUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Account]:
    """
    update existing account
    """
    result = await crud.account.update(sess, account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.AccountDict)
async def delete_account(
        *,
        account_in: schema.AccountDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[Dict]:
    """
    delete one account
    """
    result = await crud.account.delete(sess, account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result