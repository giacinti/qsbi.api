from datetime import datetime
from typing import Any, Optional,Sequence
from pydantic import BaseModel,root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_all_non_null

class AuditLog(BaseQsbi):
    id: Optional[int]
    user_id: Optional[int]
    date: Optional[datetime]
    notes: Optional[str]

class AuditLogCreate(AuditLog):
    @root_validator
    def AuditLogCreate_validate(cls, values) -> Any:
        if values.get('date') is None:
            values['date']=datetime.utcnow()
        return check_all_non_null(values,'user','date')

class AuditLogRead(BaseAny):
    id: int

class AuditLogUpdate(AuditLog,BaseId):
    pass

class AuditLogDelete(AuditLogRead):
    pass
