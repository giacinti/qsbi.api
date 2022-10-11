from fastapi import APIRouter, HTTPException, Security
from typing import Optional, List

import qsbi.api.schemas.reconcile as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()


@router.post("", status_code=201, response_model=schema.Reconcile)
async def create_reconcile(
        *,
        reconcile_in: schema.ReconcileCreate,
        curr_user=Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Reconcile:
    """
    create a new reconcile
    """
    reconcile: schema.Reconcile = await crud.reconcile.create(reconcile_in)
    return reconcile


@router.get("/list", status_code=200, response_model=List[schema.Reconcile])
async def list_reconciles(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Reconcile]:
    """
    list all reconciles
    """
    reconciles: List[schema.Reconcile] = await crud.reconcile.list(skip, limit)
    return reconciles


@router.post("/search", status_code=200, response_model=List[schema.Reconcile])
async def search_reconciles(
        *,
        reconcile_in: schema.Reconcile,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Reconcile]:
    """
    search reconciles
    """
    reconciles: List[schema.Reconcile] = await crud.reconcile.search(reconcile_in, limit)
    return reconciles


@router.get("/id/{id}", status_code=200, response_model=schema.Reconcile)
async def get_reconcile_by_id(
        *,
        id: int,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Reconcile]:
    """
    get reconcile by id
    """
    result: Optional[schema.Reconcile] = await crud.reconcile.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile with id {id} not found"
        )
    return result


@router.get("/count", status_code=200, response_model=int)
async def count_reconciles(
        *,
        curr_user=Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all reconciles
    """
    count: int = await crud.reconcile.count()
    return count


@router.put("", status_code=201, response_model=schema.Reconcile)
async def update_reconcile(
        *,
        reconcile_in: schema.ReconcileUpdate,
        curr_user=Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Reconcile]:
    """
    update existing reconcile
    """
    result: Optional[schema.Reconcile] = await crud.reconcile.update(reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result


@router.delete("", status_code=200, response_model=schema.Reconcile)
async def delete_reconcile(
        *,
        reconcile_in: schema.ReconcileDelete,
        curr_user=Security(auth.get_current_active_user, scopes=["delete"]),
        ) -> Optional[schema.Reconcile]:
    """
    delete one reconcile
    """
    result: Optional[schema.Reconcile] = await crud.reconcile.delete(reconcile_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Reconcile {reconcile_in} not found"
        )
    return result
