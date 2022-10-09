from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.scheduled as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.Scheduled)
async def create_scheduled(
        *,
        scheduled_in: schema.ScheduledCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Scheduled:
    """
    create a new scheduled
    """
    scheduled: schema.Scheduled  = await crud.scheduled.create(scheduled_in)
    return scheduled

## READ
@router.get("/list", status_code=200, response_model=List[schema.Scheduled])
async def list_scheduleds(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Scheduled]:
    """
    list all scheduleds
    """
    scheduleds: List[schema.Scheduled] = await crud.scheduled.list(skip, limit)
    return scheduleds

@router.post("/search", status_code=200, response_model=List[schema.Scheduled])
async def search_scheduleds(
        *,
        scheduled_in: schema.Scheduled,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Scheduled]:
    """
    search scheduleds
    """
    scheduleds: List[schema.Scheduled] = await crud.scheduled.search(scheduled_in, limit)
    return scheduleds

@router.get("/id/{id}", status_code=200, response_model=schema.Scheduled)
async def get_scheduled_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Scheduled]:
    """
    get scheduled by id
    """
    result: Optional[schema.Scheduled] = await crud.scheduled.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_scheduleds(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all scheduleds
    """
    count: int = await crud.scheduled.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.Scheduled)
async def update_scheduled(
        *,
        scheduled_in: schema.ScheduledUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Scheduled]:
    """
    update existing scheduled
    """
    result: Optional[schema.Scheduled] = await crud.scheduled.update(scheduled_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled {scheduled_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.Scheduled)
async def delete_scheduled(
        *,
        scheduled_in: schema.ScheduledDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.Scheduled]:
    """
    delete one scheduled
    """
    result: Optional[schema.Scheduled] = await crud.scheduled.delete(scheduled_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled {scheduled_in} not found"
        )
    return result