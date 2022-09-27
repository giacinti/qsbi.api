from datetime import datetime
from typing import Optional, Sequence
from pydantic import BaseModel, root_validator

from .base import BaseQsbi, BaseAny, BaseIdOrName, BaseGet, check_one_non_null, check_all_non_null
from .account_type import AccountType
from .currency import Currency
from .bank import Bank

##############################################################################
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

# returned by delete
class AccountDict(BaseModel):
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
    def AccountCreate_validate(cls, values):
        return check_all_non_null(values,'name')

class AccountRead(Account,BaseAny):
    pass

class AccountUpdate(Account,BaseIdOrName):
    pass

class AccountDelete(BaseIdOrName):
    id: Optional[int]
    name: Optional[str]

        
class AccountSeq(BaseModel):
    results: Sequence[Account]

