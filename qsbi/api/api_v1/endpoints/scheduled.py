from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.scheduled
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.scheduled.Scheduled)
def create_scheduled(
        *,
        scheduled_in: qsbi.api.schemas.scheduled.ScheduledCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.scheduled.Scheduled:
    """
    create a new scheduled
    """
    scheduled = qsbi.crud.scheduled.create(sess, scheduled_in)
    return scheduled

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.scheduled.ScheduledSeq)
def list_scheduleds(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.scheduled.ScheduledSeq:
    """
    list all scheduleds
    """
    scheduleds = qsbi.crud.scheduled.list(sess, skip, limit)
    return {"results": scheduleds}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.scheduled.ScheduledSeq)
def search_scheduleds(
        *,
        scheduled_in: qsbi.api.schemas.scheduled.ScheduledRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.scheduled.ScheduledSeq:
    """
    search scheduleds
    """
    scheduleds = qsbi.crud.scheduled.search(sess, scheduled_in, limit)
    return {"results": scheduleds}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.scheduled.Scheduled)
def get_scheduled_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.scheduled.Scheduled]:
    """
    get scheduled by id
    """
    result = qsbi.crud.scheduled.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.scheduled.Scheduled)
def update_scheduled(
        *,
        scheduled_in: qsbi.api.schemas.scheduled.ScheduledUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.scheduled.Scheduled]:
    """
    update existing scheduled
    """
    result = qsbi.crud.scheduled.update(sess, scheduled_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled {scheduled_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.scheduled.ScheduledDict)
def delete_scheduled(
        *,
        scheduled_in: qsbi.api.schemas.scheduled.ScheduledDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one scheduled
    """
    result = qsbi.crud.scheduled.delete(sess, scheduled_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Scheduled {scheduled_in} not found"
        )
    return result
