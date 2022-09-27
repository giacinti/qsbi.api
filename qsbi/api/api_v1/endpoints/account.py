from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.account as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Account)
def create_account(
        *,
        account_in: schema.AccountCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Account:
    """
    create a new account
    """
    account = crud.account.create(sess, account_in)
    return account

## READ
@router.get("/list", status_code=200, response_model=schema.AccountSeq)
def list_accounts(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.AccountSeq:
    """
    list all accounts
    """
    accounts = crud.account.list(sess, skip, limit)
    return {"results": accounts}

@router.post("/search", status_code=200, response_model=schema.AccountSeq)
def search_accounts(
        *,
        account_in: schema.AccountRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.AccountSeq:
    """
    search accounts
    """
    accounts = crud.account.search(sess, account_in, limit)
    return {"results": accounts}

@router.get("/id/{id}", status_code=200, response_model=schema.Account)
def get_account_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Account]:
    """
    get account by id
    """
    result = crud.account.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Account)
def get_account_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Account]:
    """
    get account by name
    """
    result = crud.account.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Account)
def update_account(
        *,
        account_in: schema.AccountUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Account]:
    """
    update existing account
    """
    result = crud.account.update(sess, account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.AccountDict)
def delete_account(
        *,
        account_in: schema.AccountDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one account
    """
    result = crud.account.delete(sess, account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result
