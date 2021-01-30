from pydantic import BaseModel
from typing import Optional, List


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        schema_extra = {
            'example': {
                'access_token': 'eyJhbGciOiJIUzI1NiIsI...',
                'token_type': 'bearer'
            }
        }


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []
