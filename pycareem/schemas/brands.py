from pydantic import BaseModel
from typing import Any
from ..branches import CareemBranches


class CareemBrandBase(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class CareemBrandCreate(CareemBrandBase):
    pass


class CareemBrandResponse(CareemBrandBase):
    created_at: str
    updated_at: str
    client: Any
    branches: Any
    careem: Any

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = kwargs['client']
        self.careem = kwargs['careem']
        self.branches = CareemBranches(self.client, brand_id=self.id, careem=self.careem)

    def delete(self):
        self.client.delete(self.id)

    def update(self, name):
        self.client.update(self.id, name)
