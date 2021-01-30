from pydantic import BaseModel


class Detail(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "detail": "Could not validate credentials"
            }
        }
