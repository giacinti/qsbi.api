from datetime import datetime
from typing import Any, Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseId, check_all_non_null

class Scheduled(BaseQsbi):
    id : Optional[int]
    account_id : Optional[int]
    start_date : Optional[datetime]
    limit_date : Optional[datetime]
    frequency : Optional[int]
    automatic : Optional[bool] = False
    party_id : Optional[int]
    category_id : Optional[int]
    sub_category_id : Optional[int]
    notes : Optional[str]
    amount : Optional[float]
    currency_id : Optional[int]
    payment_id : Optional[int]
    splitted : Optional[bool] = False
    master_id : Optional[int]
    log_id : Optional[int]

    @root_validator
    def Scheduled_validate(cls,values) -> Any:
        if values.get('splitted') == True:
            if values.get('master') is None:
                raise ValueError("master is needed if splitted is set to True")
        return values

class ScheduledCreate(Scheduled):
    @root_validator
    def ScheduledCreate_validate(cls, values) -> Any:
        return check_all_non_null(values,'account','log')

class ScheduledRead(BaseAny):
    id : int

class ScheduledUpdate(Scheduled,BaseId):
    pass

class ScheduledDelete(ScheduledRead):
    pass

