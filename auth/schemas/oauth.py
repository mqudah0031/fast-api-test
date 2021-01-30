from pydantic import BaseModel
from enum import Enum
from typing import Optional


class ResponseTypeEnum(Enum):
    code = 'code'


class Authorize(BaseModel):
    client_id: str
    redirect_uri: str
    response_type: ResponseTypeEnum
    scope: Optional[str]
