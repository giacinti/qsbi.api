from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.audit_log as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.AuditLog)
async def create_audit_log(
        *,
        audit_log_in: schema.AuditLogCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.AuditLog:
    """
    create a new audit_log
    """
    audit_log: schema.AuditLog  = await crud.audit_log.create(audit_log_in)
    return audit_log

## READ
@router.get("/list", status_code=200, response_model=List[schema.AuditLog])
async def list_audit_logs(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.AuditLog]:
    """
    list all audit_logs
    """
    audit_logs: List[schema.AuditLog] = await crud.audit_log.list(skip, limit)
    return audit_logs

@router.post("/search", status_code=200, response_model=List[schema.AuditLog])
async def search_audit_logs(
        *,
        audit_log_in: schema.AuditLog,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.AuditLog]:
    """
    search audit_logs
    """
    audit_logs: List[schema.AuditLog] = await crud.audit_log.search(audit_log_in, limit)
    return audit_logs

@router.get("/id/{id}", status_code=200, response_model=schema.AuditLog)
async def get_audit_log_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.AuditLog]:
    """
    get audit_log by id
    """
    result: Optional[schema.AuditLog] = await crud.audit_log.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_audit_logs(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all audit_logs
    """
    count: int = await crud.audit_log.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.AuditLog)
async def update_audit_log(
        *,
        audit_log_in: schema.AuditLogUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.AuditLog]:
    """
    update existing audit_log
    """
    result: Optional[schema.AuditLog] = await crud.audit_log.update(audit_log_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog {audit_log_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.AuditLog)
async def delete_audit_log(
        *,
        audit_log_in: schema.AuditLogDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.AuditLog]:
    """
    delete one audit_log
    """
    result: Optional[schema.AuditLog] = await crud.audit_log.delete(audit_log_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"AuditLog {audit_log_in} not found"
        )
    return result