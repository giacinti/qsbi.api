from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.audit_log as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.AuditLog)
def create_audit_log(
        *,
        audit_log_in: schema.AuditLogCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.AuditLog:
    """
    create a new audit_log
    """
    audit_log = crud.audit_log.create(sess, audit_log_in)
    return audit_log

## READ
@router.get("/list", status_code=200, response_model=schema.AuditLogSeq)
def list_audit_logs(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.AuditLogSeq:
    """
    list all audit_logs
    """
    audit_logs = crud.audit_log.list(sess, skip, limit)
    return {"results": audit_logs}

@router.post("/search", status_code=200, response_model=schema.AuditLogSeq)
def search_audit_logs(
        *,
        audit_log_in: schema.AuditLogRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.AuditLogSeq:
    """
    search audit_logs
    """
    audit_logs = crud.audit_log.search(sess, audit_log_in, limit)
    return {"results": audit_logs}

@router.get("/id/{id}", status_code=200, response_model=schema.AuditLog)
def get_audit_log_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.AuditLog]:
    """
    get audit_log by id
    """
    result = crud.audit_log.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.AuditLog)
def update_audit_log(
        *,
        audit_log_in: schema.AuditLogUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.AuditLog]:
    """
    update existing audit_log
    """
    result = crud.audit_log.update(sess, audit_log_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog {audit_log_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.AuditLogDict)
def delete_audit_log(
        *,
        audit_log_in: schema.AuditLogDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one audit_log
    """
    result = crud.audit_log.delete(sess, audit_log_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog {audit_log_in} not found"
        )
    return result
