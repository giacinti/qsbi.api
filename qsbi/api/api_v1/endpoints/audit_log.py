from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.audit_log
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.audit_log.AuditLog)
def create_audit_log(
        *,
        audit_log_in: qsbi.api.schemas.audit_log.AuditLogCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.audit_log.AuditLog:
    """
    create a new audit_log
    """
    audit_log = qsbi.crud.audit_log.create(sess, audit_log_in)
    return audit_log

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.audit_log.AuditLogSeq)
def list_audit_logs(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.audit_log.AuditLogSeq:
    """
    list all audit_logs
    """
    audit_logs = qsbi.crud.audit_log.list(sess, skip, limit)
    return {"results": audit_logs}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.audit_log.AuditLogSeq)
def search_audit_logs(
        *,
        audit_log_in: qsbi.api.schemas.audit_log.AuditLogRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.audit_log.AuditLogSeq:
    """
    search audit_logs
    """
    audit_logs = qsbi.crud.audit_log.search(sess, audit_log_in, limit)
    return {"results": audit_logs}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.audit_log.AuditLog)
def get_audit_log_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.audit_log.AuditLog]:
    """
    get audit_log by id
    """
    result = qsbi.crud.audit_log.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.audit_log.AuditLog)
def update_audit_log(
        *,
        audit_log_in: qsbi.api.schemas.audit_log.AuditLogUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.audit_log.AuditLog]:
    """
    update existing audit_log
    """
    result = qsbi.crud.audit_log.update(sess, audit_log_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog {audit_log_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.audit_log.AuditLogDict)
def delete_audit_log(
        *,
        audit_log_in: qsbi.api.schemas.audit_log.AuditLogDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one audit_log
    """
    result = qsbi.crud.audit_log.delete(sess, audit_log_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog {audit_log_in} not found"
        )
    return result
