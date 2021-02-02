from pydantic import BaseModel


class CareemIdentityToken(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    scope: str

    class Config:
        orm_mode = True
