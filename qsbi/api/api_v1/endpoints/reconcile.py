from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.reconcile as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.Reconcile)
async def create_reconcile(
        *,
        reconcile_in: schema.ReconcileCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Reconcile:
    """
    create a new reconcile
    """
    reconcile = await crud.reconcile.create(sess, reconcile_in)
    return reconcile

## READ
@router.get("/list", status_code=200, response_model=schema.ReconcileSeq)
async def list_reconciles(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.ReconcileSeq:
    """
    list all reconciles
    """
    reconciles = await crud.reconcile.list(sess, skip, limit)
    return {"results": reconciles}

@router.post("/search", status_code=200, response_model=schema.ReconcileSeq)
async def search_reconciles(
        *,
        reconcile_in: schema.ReconcileRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.ReconcileSeq:
    """
    search reconciles
    """
    reconciles = await crud.reconcile.search(sess, reconcile_in, limit)
    return {"results": reconciles}

@router.get("/id/{id}", status_code=200, response_model=schema.Reconcile)
async def get_reconcile_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Reconcile]:
    """
    get reconcile by id
    """
    result = await crud.reconcile.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_reconciles(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all reconciles
    """
    count = await crud.reconcile.count(sess)
    return {"count": count}

## UPDATE
@router.put("", status_code=201, response_model=schema.Reconcile)
async def update_reconcile(
        *,
        reconcile_in: schema.ReconcileUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Reconcile]:
    """
    update existing reconcile
    """
    result = await crud.reconcile.update(sess, reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.ReconcileDict)
async def delete_reconcile(
        *,
        reconcile_in: schema.ReconcileDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[Dict]:
    """
    delete one reconcile
    """
    result = await crud.reconcile.delete(sess, reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result