from abc import ABC, abstractmethod
from typing import Any, List, Optional

class QsbiCRUD(ABC):
    @abstractmethod
    async def get_by(self, attr: str, val: Any) -> Any:
        pass

    @abstractmethod
    async def list(self, skip: Optional[int]=0, limit: Optional[int]=100) -> List:
        pass

    @abstractmethod
    async def create(self, obj_in: Any) -> Any:
        pass

    @abstractmethod
    async def search(self, obj_in: Any, limit: Optional[int]=100) -> List:
        pass

    @abstractmethod
    async def update(self, obj_in: Any) -> Any:
        pass

    @abstractmethod
    async def delete(self, obj_in: Any) -> Any:
        pass

    @abstractmethod
    async def count(self) -> int:
        pass

account: QsbiCRUD = None  # type: ignore
account_type: QsbiCRUD = None  # type: ignore
audit_log: QsbiCRUD = None  # type: ignore
bank: QsbiCRUD = None  # type: ignore
category: QsbiCRUD = None  # type: ignore
currency_link: QsbiCRUD = None  # type: ignore
currency: QsbiCRUD = None  # type: ignore
party: QsbiCRUD = None  # type: ignore
payment: QsbiCRUD = None  # type: ignore
payment_type: QsbiCRUD = None  # type: ignore
reconcile: QsbiCRUD = None  # type: ignore
scheduled: QsbiCRUD = None  # type: ignore
sub_category: QsbiCRUD = None  # type: ignore
transact: QsbiCRUD = None  # type: ignore
user: QsbiCRUD = None  # type: ignore

