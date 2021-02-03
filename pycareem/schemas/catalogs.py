from pydantic import BaseModel
from typing import Any, List


class Catalog(BaseModel):
    id: str
    name: str
    include_tax: bool
    tax: float
    avg_price: float
    file: str
    currency_id: int
    category_ids: List[str]


class Shift(BaseModel):
    start_time: str
    end_time: str


class OperationalHours(BaseModel):
    shifts: List[Shift]
    active: bool
    day_of_week: int

    class Config:
        orm_mode = True


class Category(BaseModel):
    id: str
    deleted: bool
    name: str
    name_localized: dict
    description: str
    description_localized: dict
    preparation_time: int
    priority: int
    operational_hours: List[OperationalHours]
    items: List[str]

    class Config:
        orm_mode = True


class Item(BaseModel):
    id: str
    deleted: bool
    name: str
    name_localized: dict
    description: str
    description_localized: dict
    active: bool
    price: int
    calorie_counts: str
    allergic_information: str
    operational_hours: OperationalHours
    media: str
    groups: List[str]

    class Config:
        orm_mode = True


class Group(BaseModel):
    id: str
    deleted: bool
    name: str
    name_localized: dict
    description: str
    description_localized: dict
    min: int
    max: int
    options: List[str]

    class Config:
        orm_mode = True


class Option(BaseModel):
    id: str
    deleted: bool
    name: str
    name_localized: dict
    active: bool
    price: int

    class Config:
        orm_mode = True


class CareemCatalogBase(BaseModel):
    catalog: Catalog
    categories: List[Category]
    items: List[Item]
    groups: List[Group]
    options: List[Option]

    class Config:
        orm_mode = True


class CareemCatalogCreate(CareemCatalogBase):
    diff: bool


class CareemCatalogResponse(CareemCatalogBase):
    client: Any
    careem: Any

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = kwargs['client']

    def delete(self):
        self.client.delete(self.catalog.id)

    def update(self, name):
        self.client.update(self.catalog.id, name)
