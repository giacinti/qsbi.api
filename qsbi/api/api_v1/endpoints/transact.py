from fastapi import APIRouter, HTTPException, Security
from typing import Optional, List

import qsbi.api.schemas.transact as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()


@router.post("", status_code=201, response_model=schema.Transact)
async def create_transact(
        *,
        transact_in: schema.TransactCreate,
        curr_user=Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Transact:
    """
    create a new transact
    """
    transact: schema.Transact = await crud.transact.create(transact_in)
    return transact


@router.get("/list", status_code=200, response_model=List[schema.Transact])
async def list_transacts(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Transact]:
    """
    list all transacts
    """
    transacts: List[schema.Transact] = await crud.transact.list(skip, limit)
    return transacts


@router.post("/search", status_code=200, response_model=List[schema.Transact])
async def search_transacts(
        *,
        transact_in: schema.Transact,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Transact]:
    """
    search transacts
    """
    transacts: List[schema.Transact] = await crud.transact.search(transact_in, limit)
    return transacts


@router.get("/id/{id}", status_code=200, response_model=schema.Transact)
async def get_transact_by_id(
        *,
        id: int,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Transact]:
    """
    get transact by id
    """
    result: Optional[schema.Transact] = await crud.transact.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact with id {id} not found"
        )
    return result


@router.get("/count", status_code=200, response_model=int)
async def count_transacts(
        *,
        curr_user=Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all transacts
    """
    count: int = await crud.transact.count()
    return count


@router.put("", status_code=201, response_model=schema.Transact)
async def update_transact(
        *,
        transact_in: schema.TransactUpdate,
        curr_user=Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Transact]:
    """
    update existing transact
    """
    result: Optional[schema.Transact] = await crud.transact.update(transact_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact {transact_in} not found"
        )
    return result


@router.delete("", status_code=200, response_model=schema.Transact)
async def delete_transact(
        *,
        transact_in: schema.TransactDelete,
        curr_user=Security(auth.get_current_active_user, scopes=["delete"]),
        ) -> Optional[schema.Transact]:
    """
    delete one transact
    """
    result: Optional[schema.Transact] = await crud.transact.delete(transact_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Transact {transact_in} not found"
        )
    return result
