from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.transact as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Transact)
async def create_transact(
        *,
        transact_in: schema.TransactCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Transact:
    """
    create a new transact
    """
    transact = await crud.transact.create(sess, transact_in)
    return transact

## READ
@router.get("/list", status_code=200, response_model=schema.TransactSeq)
async def list_transacts(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.TransactSeq:
    """
    list all transacts
    """
    transacts = await crud.transact.list(sess, skip, limit)
    return {"results": transacts}

@router.post("/search", status_code=200, response_model=schema.TransactSeq)
async def search_transacts(
        *,
        transact_in: schema.TransactRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.TransactSeq:
    """
    search transacts
    """
    transacts = await crud.transact.search(sess, transact_in, limit)
    return {"results": transacts}

@router.get("/id/{id}", status_code=200, response_model=schema.Transact)
async def get_transact_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Transact]:
    """
    get transact by id
    """
    result = await crud.transact.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_transacts(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all transacts
    """
    count = await crud.transact.count(sess)
    return {"count": count}

## UPDATE
@router.put("/", status_code=201, response_model=schema.Transact)
async def update_transact(
        *,
        transact_in: schema.TransactUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Transact]:
    """
    update existing transact
    """
    result = await crud.transact.update(sess, transact_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact {transact_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.TransactDict)
async def delete_transact(
        *,
        transact_in: schema.TransactDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one transact
    """
    result = await crud.transact.delete(sess, transact_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact {transact_in} not found"
        )
    return result