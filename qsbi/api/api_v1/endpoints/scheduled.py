from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.scheduled as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Scheduled)
def create_scheduled(
        *,
        scheduled_in: schema.ScheduledCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Scheduled:
    """
    create a new scheduled
    """
    scheduled = crud.scheduled.create(sess, scheduled_in)
    return scheduled

## READ
@router.get("/list", status_code=200, response_model=schema.ScheduledSeq)
def list_scheduleds(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.ScheduledSeq:
    """
    list all scheduleds
    """
    scheduleds = crud.scheduled.list(sess, skip, limit)
    return {"results": scheduleds}

@router.post("/search", status_code=200, response_model=schema.ScheduledSeq)
def search_scheduleds(
        *,
        scheduled_in: schema.ScheduledRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.ScheduledSeq:
    """
    search scheduleds
    """
    scheduleds = crud.scheduled.search(sess, scheduled_in, limit)
    return {"results": scheduleds}

@router.get("/id/{id}", status_code=200, response_model=schema.Scheduled)
def get_scheduled_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Scheduled]:
    """
    get scheduled by id
    """
    result = crud.scheduled.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Scheduled)
def update_scheduled(
        *,
        scheduled_in: schema.ScheduledUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Scheduled]:
    """
    update existing scheduled
    """
    result = crud.scheduled.update(sess, scheduled_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled {scheduled_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.ScheduledDict)
def delete_scheduled(
        *,
        scheduled_in: schema.ScheduledDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one scheduled
    """
    result = crud.scheduled.delete(sess, scheduled_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled {scheduled_in} not found"
        )
    return result
