import pathlib
from pydantic import BaseSettings, AnyHttpUrl, validator
from typing import Union, List


# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    ##############################################################################
    API_V1_STR: str = "/api/v1"

    ##############################################################################
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    ##############################################################################
    QSBI_JWT_SECRET_KEY: str = None
    @validator("QSBI_JWT_SECRET_KEY", pre=True)
    def check_jwt_secret_key(cls, v: str) -> str:
        if v is not None:
            return v
        else:
            raise ValueError(v)
        
    QSBI_JWT_ALGORITHM: str = "HS256"
    QSBI_JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    

    ##############################################################################
    class Config:
        case_sensitive = True


settings = Settings()
