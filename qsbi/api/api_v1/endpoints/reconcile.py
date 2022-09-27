from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.reconcile
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.reconcile.Reconcile)
def create_reconcile(
        *,
        reconcile_in: qsbi.api.schemas.reconcile.ReconcileCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.reconcile.Reconcile:
    """
    create a new reconcile
    """
    reconcile = qsbi.crud.reconcile.create(sess, reconcile_in)
    return reconcile

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.reconcile.ReconcileSeq)
def list_reconciles(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.reconcile.ReconcileSeq:
    """
    list all reconciles
    """
    reconciles = qsbi.crud.reconcile.list(sess, skip, limit)
    return {"results": reconciles}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.reconcile.ReconcileSeq)
def search_reconciles(
        *,
        reconcile_in: qsbi.api.schemas.reconcile.ReconcileRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.reconcile.ReconcileSeq:
    """
    search reconciles
    """
    reconciles = qsbi.crud.reconcile.search(sess, reconcile_in, limit)
    return {"results": reconciles}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.reconcile.Reconcile)
def get_reconcile_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.reconcile.Reconcile]:
    """
    get reconcile by id
    """
    result = qsbi.crud.reconcile.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.reconcile.Reconcile)
def update_reconcile(
        *,
        reconcile_in: qsbi.api.schemas.reconcile.ReconcileUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.reconcile.Reconcile]:
    """
    update existing reconcile
    """
    result = qsbi.crud.reconcile.update(sess, reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.reconcile.ReconcileDict)
def delete_reconcile(
        *,
        reconcile_in: qsbi.api.schemas.reconcile.ReconcileDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one reconcile
    """
    result = qsbi.crud.reconcile.delete(sess, reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result
