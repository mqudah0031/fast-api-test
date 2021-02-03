from pydantic import BaseModel
from typing import Any


class CareemBranchBase(BaseModel):
    id: str
    name: str
    brand_id: str
    state: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True


class CareemBranchCreate(CareemBranchBase):
    pass


class CareemBranchResponse(CareemBranchBase):
    client: Any
    careem: Any
    catalogs: Any

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = kwargs['client']
        self.catalogs = CareemCatalogs(careem=self.careem, client=self.client, branch_id=self.brand_id)

    def delete(self):
        self.client.delete(self.id)

    def update(self, name):
        self.client.update(self.id, name)
