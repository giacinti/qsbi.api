from datetime import datetime
from typing import Optional,Sequence
from pydantic import BaseModel,root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_one_non_null, check_all_non_null
from .user import User

class AuditLog(BaseQsbi):
    id: Optional[int]
    user_id: Optional[int]
    date: Optional[datetime]
    notes: Optional[str]

class AuditLogDict(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    date: Optional[datetime]
    notes: Optional[str]

class AuditLogCreate(AuditLog):
    @root_validator
    def AuditLogCreate_validate(cls, values):
        if values.get('date') is None:
            values['date']=datetime.utcnow()
        return check_all_non_null(values,'user','date')

class AuditLogRead(AuditLog,BaseAny):
    pass

class AuditLogUpdate(AuditLog,BaseId):
    pass

class AuditLogDelete(BaseId):
    id: Optional[int]
        
class AuditLogSeq(BaseModel):
    results: Sequence[AuditLog]

