from fastapi import APIRouter

from qsbi.api.api_v1.adm_endpoints import token
from qsbi.api.api_v1.adm_endpoints import user

qsbi_admin_router = APIRouter()
qsbi_admin_router.include_router(token.router, prefix="/token", tags=["Token"])
qsbi_admin_router.include_router(user.router, prefix="/user", tags=["User"])
