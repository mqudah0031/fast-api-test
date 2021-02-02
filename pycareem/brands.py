import requests
from .schemas.brands import CareemBrandCreate, CareemBrandResponse
from .schemas import Pagination
from .exceptions.brands import BrandNotFound
from .branches import CareemBranches


class CareemBrands:

    def __init__(self, careem):
        self.careem = careem

    def create(self, _id, name) -> CareemBrandResponse:
        payload = CareemBrandCreate(id=_id, name=name)
        response = self.careem.post(f"{self.careem.base_url}/brands", data=payload)
        return CareemBrandResponse(**response.json(), client=self, careem=self.careem)

    def list(self) -> Pagination:
        response = self.careem.get(f"{self.careem.base_url}/brands")
        _json = response.json()
        _json['data'] = list(
            map(lambda _: CareemBrandResponse(**_, client=self, careem=self.careem), [j for j in _json['data']]))
        return Pagination(**_json)

    def get(self, _id) -> CareemBrandResponse:
        response = self.careem.get(f"{self.careem.base_url}/brands/{_id}")
        if response.status_code == 404:
            raise BrandNotFound
        return CareemBrandResponse(**response.json(), client=self, careem=self.careem)

    def update(self, _id) -> CareemBrandResponse:
        # TODO:
        response = self.careem.get(f"{self.careem.base_url}/brands/{_id}")
        if response.status_code == 404:
            raise BrandNotFound
        return CareemBrandResponse(**response.json(), careem=self.careem)
