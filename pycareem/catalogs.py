from .schemas.catalogs import CareemBranchResponse
from .schemas import Pagination
from .exceptions.branches import BranchNotFound


class CareemCatalogs:

    def __init__(self, client, brand_id, careem):
        # branches api
        self.client = client
        self.brand_id = brand_id
        self.careem = careem

    def list(self) -> Pagination:
        headers = {'Brand-Id': self.brand_id}
        response = self.careem.get(f"{self.careem.base_url}/branches", headers=headers)
        _json = response.json()
        _json['data'] = list(
            map(lambda _: CareemBranchResponse(**_, client=self, careem=self.careem, brand_id=self.brand_id), _json['data']))
        return Pagination(**_json)

    def get(self, _id) -> CareemBranchResponse:
        headers = {'Brand-Id': self.brand_id}
        response = self.careem.get(f"{self.careem.base_url}/branches/{_id}", headers=headers)
        if response.status_code == 404:
            raise BranchNotFound
        return CareemBranchResponse(**response.json(), client=self, careem=self.careem, brand_id=self.brand_id)

    def update(self, _id, name: str) -> CareemBranchResponse:
        headers = {'Brand-Id': self.brand_id, 'Content-Type': 'application/json'}
        import json
        payload = json.dumps({'name': name})
        response = self.careem.put(f"{self.careem.base_url}/branches/{_id}", headers=headers, data=payload)
        if response.status_code == 404:
            raise BranchNotFound
        return CareemBranchResponse(**response.json(), client=self, careem=self.careem)

    def create(self, name: str) -> CareemBranchResponse:
        import uuid
        _id = str(uuid.uuid4())
        return self.update(_id, name)
