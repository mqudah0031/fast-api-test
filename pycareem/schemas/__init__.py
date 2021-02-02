from pydantic import BaseModel
from typing import List, Dict, Optional


class PaginationMeta(BaseModel):
    total: int
    page_size: int
    page_number: int


class PaginationList(BaseModel):
    prev: Optional[str]
    next: Optional[str]


class Pagination(BaseModel):
    data: List
    meta: PaginationMeta
    links: PaginationList
