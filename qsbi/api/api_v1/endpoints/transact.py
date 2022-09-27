from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.transact
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.transact.Transact)
def create_transact(
        *,
        transact_in: qsbi.api.schemas.transact.TransactCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.transact.Transact:
    """
    create a new transact
    """
    transact = qsbi.crud.transact.create(sess, transact_in)
    return transact

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.transact.TransactSeq)
def list_transacts(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.transact.TransactSeq:
    """
    list all transacts
    """
    transacts = qsbi.crud.transact.list(sess, skip, limit)
    return {"results": transacts}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.transact.TransactSeq)
def search_transacts(
        *,
        transact_in: qsbi.api.schemas.transact.TransactRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.transact.TransactSeq:
    """
    search transacts
    """
    transacts = qsbi.crud.transact.search(sess, transact_in, limit)
    return {"results": transacts}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.transact.Transact)
def get_transact_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.transact.Transact]:
    """
    get transact by id
    """
    result = qsbi.crud.transact.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.transact.Transact)
def update_transact(
        *,
        transact_in: qsbi.api.schemas.transact.TransactUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.transact.Transact]:
    """
    update existing transact
    """
    result = qsbi.crud.transact.update(sess, transact_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact {transact_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.transact.TransactDict)
def delete_transact(
        *,
        transact_in: qsbi.api.schemas.transact.TransactDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one transact
    """
    result = qsbi.crud.transact.delete(sess, transact_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact {transact_in} not found"
        )
    return result
