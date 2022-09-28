from fastapi import FastAPI

from qsbi.api.config import settings
from qsbi.api.api_v1.api import qsbi_api_router


qsbi_api = FastAPI(title="QSBI API",
                   description="QSBI is not Qu\*ck\*n nor Gr\*sb\*",
                   version="1.0",
                   contact={
                       "name": "Philippe Giacinti",
                       "url": "http://www.giacinti.fr",
                       "email": "philippe@giacinti.com",
                       },
                   openapi_url=f"{settings.API_V1_STR}/openapi.json")

qsbi_api.include_router(qsbi_api_router, prefix=settings.API_V1_STR)

