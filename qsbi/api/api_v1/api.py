from fastapi import APIRouter

from qsbi.api.api_v1.endpoints import account
from qsbi.api.api_v1.endpoints import account_type
from qsbi.api.api_v1.endpoints import audit_log
from qsbi.api.api_v1.endpoints import bank
from qsbi.api.api_v1.endpoints import category
from qsbi.api.api_v1.endpoints import currency
from qsbi.api.api_v1.endpoints import currency_link
from qsbi.api.api_v1.endpoints import party
from qsbi.api.api_v1.endpoints import payment
from qsbi.api.api_v1.endpoints import payment_type
from qsbi.api.api_v1.endpoints import reconcile
from qsbi.api.api_v1.endpoints import scheduled
from qsbi.api.api_v1.endpoints import sub_category
from qsbi.api.api_v1.endpoints import transact
from qsbi.api.api_v1.endpoints import user

qsbi_api_router = APIRouter()
qsbi_api_router.include_router(account.router, prefix="/account", tags=["Account"])
qsbi_api_router.include_router(account_type.router, prefix="/account_type", tags=["Account Type"])
qsbi_api_router.include_router(audit_log.router, prefix="/audit_log", tags=["Audit Log"])
qsbi_api_router.include_router(bank.router, prefix="/bank", tags=["Bank"])
qsbi_api_router.include_router(category.router, prefix="/category", tags=["Category"])
qsbi_api_router.include_router(currency.router, prefix="/currency", tags=["Currency"])
qsbi_api_router.include_router(currency_link.router, prefix="/currency_link", tags=["Currencies Link"])
qsbi_api_router.include_router(party.router, prefix="/party", tags=["Party"])
qsbi_api_router.include_router(payment.router, prefix="/payment", tags=["Payment"])
qsbi_api_router.include_router(payment_type.router, prefix="/payment_type", tags=["Payment Type"])
qsbi_api_router.include_router(reconcile.router, prefix="/reconcile", tags=["Reconcile"])
qsbi_api_router.include_router(scheduled.router, prefix="/scheduled", tags=["Scheduled"])
qsbi_api_router.include_router(sub_category.router, prefix="/sub_category", tags=["Sub Category"])
qsbi_api_router.include_router(transact.router, prefix="/transact", tags=["Transaction"])
qsbi_api_router.include_router(user.router, prefix="/user", tags=["User"])
