from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.account
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.account.Account)
def create_account(
        *,
        account_in: qsbi.api.schemas.account.AccountCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.account.Account:
    """
    create a new account
    """
    account = qsbi.crud.account.create(sess, account_in)
    return account

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.account.AccountSeq)
def list_accounts(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.account.AccountSeq:
    """
    list all accounts
    """
    accounts = qsbi.crud.account.list(sess, skip, limit)
    return {"results": accounts}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.account.AccountSeq)
def search_accounts(
        *,
        account_in: qsbi.api.schemas.account.AccountRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.account.AccountSeq:
    """
    search accounts
    """
    accounts = qsbi.crud.account.search(sess, account_in, limit)
    return {"results": accounts}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.account.Account)
def get_account_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.account.Account]:
    """
    get account by id
    """
    result = qsbi.crud.account.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=qsbi.api.schemas.account.Account)
def get_account_by_name(
        *,
        name: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.account.Account]:
    """
    get account by name
    """
    result = qsbi.crud.account.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.account.Account)
def update_account(
        *,
        account_in: qsbi.api.schemas.account.AccountUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.account.Account]:
    """
    update existing account
    """
    result = qsbi.crud.account.update(sess, account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.account.AccountDict)
def delete_account(
        *,
        account_in: qsbi.api.schemas.account.AccountDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one account
    """
    result = qsbi.crud.account.delete(sess, account_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Account {account_in} not found"
        )
    return result
