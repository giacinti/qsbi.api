from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.account_type
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.account_type.AccountType)
def create_account_type(
        *,
        account_type_in: qsbi.api.schemas.account_type.AccountTypeCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.account_type.AccountType:
    """
    create a new account_type
    """
    account_type = qsbi.crud.account_type.create(sess, account_type_in)
    return account_type

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.account_type.AccountTypeSeq)
def list_account_types(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.account_type.AccountTypeSeq:
    """
    list all account_types
    """
    account_types = qsbi.crud.account_type.list(sess, skip, limit)
    return {"results": account_types}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.account_type.AccountTypeSeq)
def search_account_types(
        *,
        account_type_in: qsbi.api.schemas.account_type.AccountTypeRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.account_type.AccountTypeSeq:
    """
    search account_types
    """
    account_types = qsbi.crud.account_type.search(sess, account_type_in, limit)
    return {"results": account_types}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.account_type.AccountType)
def get_account_type_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.account_type.AccountType]:
    """
    get account_type by id
    """
    result = qsbi.crud.account_type.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=qsbi.api.schemas.account_type.AccountType)
def get_account_type_by_name(
        *,
        name: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.account_type.AccountType]:
    """
    get account_type by name
    """
    result = qsbi.crud.account_type.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.account_type.AccountType)
def update_account_type(
        *,
        account_type_in: qsbi.api.schemas.account_type.AccountTypeUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.account_type.AccountType]:
    """
    update existing account_type
    """
    result = qsbi.crud.account_type.update(sess, account_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType {account_type_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.account_type.AccountTypeDict)
def delete_account_type(
        *,
        account_type_in: qsbi.api.schemas.account_type.AccountTypeDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one account_type
    """
    result = qsbi.crud.account_type.delete(sess, account_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType {account_type_in} not found"
        )
    return result
