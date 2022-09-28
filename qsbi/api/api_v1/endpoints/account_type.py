from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.account_type as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.AccountType)
async def create_account_type(
        *,
        account_type_in: schema.AccountTypeCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.AccountType:
    """
    create a new account_type
    """
    account_type = await crud.account_type.create(sess, account_type_in)
    return account_type

## READ
@router.get("/list", status_code=200, response_model=schema.AccountTypeSeq)
async def list_account_types(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.AccountTypeSeq:
    """
    list all account_types
    """
    account_types = await crud.account_type.list(sess, skip, limit)
    return {"results": account_types}

@router.post("/search", status_code=200, response_model=schema.AccountTypeSeq)
async def search_account_types(
        *,
        account_type_in: schema.AccountTypeRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.AccountTypeSeq:
    """
    search account_types
    """
    account_types = await crud.account_type.search(sess, account_type_in, limit)
    return {"results": account_types}

@router.get("/id/{id}", status_code=200, response_model=schema.AccountType)
async def get_account_type_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.AccountType]:
    """
    get account_type by id
    """
    result = await crud.account_type.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.AccountType)
async def get_account_type_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.AccountType]:
    """
    get account_type by name
    """
    result = await crud.account_type.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType with name {name} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_account_types(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all account_types
    """
    count = await crud.account_type.count(sess)
    return {"count": count}

## UPDATE
@router.put("", status_code=201, response_model=schema.AccountType)
async def update_account_type(
        *,
        account_type_in: schema.AccountTypeUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.AccountType]:
    """
    update existing account_type
    """
    result = await crud.account_type.update(sess, account_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType {account_type_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.AccountTypeDict)
async def delete_account_type(
        *,
        account_type_in: schema.AccountTypeDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[Dict]:
    """
    delete one account_type
    """
    result = await crud.account_type.delete(sess, account_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AccountType {account_type_in} not found"
        )
    return result