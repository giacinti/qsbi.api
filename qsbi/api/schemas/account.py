from datetime import datetime
from typing import Any, Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, check_all_non_null

class Account(BaseQsbi):
    id: Optional[int]
    name: Optional[str]
    bank_id: Optional[int]
    bank_branch: Optional[str]
    bank_account: Optional[str]
    bank_account_key : Optional[str]
    bank_IBAN : Optional[str]
    currency_id : Optional[int]
    open_date : Optional[datetime]
    close_date : Optional[datetime]
    type_id : Optional[int]
    initial_balance : Optional[float] = 0.0
    mini_balance_wanted : Optional[float] = 0.0
    mini_balance_auth : Optional[float] = 0.0
    holder_name : Optional[str]
    holder_address : Optional[str]
    notes : Optional[str]

class AccountCreate(Account):
    @root_validator
    def AccountCreate_validate(cls, values) -> Any:
        return check_all_non_null(values,'name')

class AccountRead(BaseAny):
    id: Optional[int]
    name: Optional[str]

class AccountUpdate(Account,BaseIdOrName):
    pass

class AccountDelete(AccountRead):
    pass
