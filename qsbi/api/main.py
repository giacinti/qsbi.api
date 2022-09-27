from fastapi import FastAPI

from qsbi.api.api_v1.api import qsbi_api_router
from qsbi.api.config import settings

qsbi_api = FastAPI(title="QSBI API", openapi_url="/openapi.json")
qsbi_api.include_router(qsbi_api_router, prefix=settings.API_V1_STR)

# if __name__ == "__main__":
#     # Use this for debugging purposes only
#     import uvicorn

#     uvicorn.run(qsbi_api, host="0.0.0.0", port=8001, log_level="debug")


