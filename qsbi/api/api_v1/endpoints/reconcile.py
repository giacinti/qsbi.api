from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.reconcile as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Reconcile)
def create_reconcile(
        *,
        reconcile_in: schema.ReconcileCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Reconcile:
    """
    create a new reconcile
    """
    reconcile = crud.reconcile.create(sess, reconcile_in)
    return reconcile

## READ
@router.get("/list", status_code=200, response_model=schema.ReconcileSeq)
def list_reconciles(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.ReconcileSeq:
    """
    list all reconciles
    """
    reconciles = crud.reconcile.list(sess, skip, limit)
    return {"results": reconciles}

@router.post("/search", status_code=200, response_model=schema.ReconcileSeq)
def search_reconciles(
        *,
        reconcile_in: schema.ReconcileRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.ReconcileSeq:
    """
    search reconciles
    """
    reconciles = crud.reconcile.search(sess, reconcile_in, limit)
    return {"results": reconciles}

@router.get("/id/{id}", status_code=200, response_model=schema.Reconcile)
def get_reconcile_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Reconcile]:
    """
    get reconcile by id
    """
    result = crud.reconcile.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Reconcile)
def update_reconcile(
        *,
        reconcile_in: schema.ReconcileUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Reconcile]:
    """
    update existing reconcile
    """
    result = crud.reconcile.update(sess, reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.ReconcileDict)
def delete_reconcile(
        *,
        reconcile_in: schema.ReconcileDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one reconcile
    """
    result = crud.reconcile.delete(sess, reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result
