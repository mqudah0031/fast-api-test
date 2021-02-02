import requests
from .schemas.auth import CareemIdentityToken
from .brands import CareemBrands


class Careem:
    base_url: str = "https://apigateway-stg.careemdash.com/pos/api/v1"
    identity_base_url: str = "https://identity.qa.careem-engineering.com"
    identity_token_api: str = f"{identity_base_url}/token"

    def __init__(self, client_id: str, client_secret: str, token=None):
        self.client_id: str = "8e810e9e-d409-46f2-a18a-5c382ceeaccb"
        self.client_secret: str = "15afae96-6bdf-49b4-be1e-bcecf46da29d"
        self.token = token
        if self.token is None:
            self.token = self.get_token()

        self.brands = CareemBrands(self)

    def get(self, *args, **kwargs):
        response = requests.get(*args, **kwargs)
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        kwargs['headers']['Authorization'] = f'Bearer {self.token}'
        if response.status_code == 401:
            # if the token is expired
            self.token = self.get_token()
            return self.get(*args, **kwargs)
        return response

    def put(self, *args, **kwargs):
        response = requests.put(*args, **kwargs)
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        kwargs['headers']['Authorization'] = f'Bearer {self.token}'
        if response.status_code == 401:
            # if the token is expired
            self.token = self.get_token()
            return self.put(*args, **kwargs)
        return response

    def post(self, *args, **kwargs):
        response = requests.get(*args, **kwargs)
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        kwargs['headers']['Authorization'] = f'Bearer {self.token}'
        if response.status_code == 401:
            # if the token is expired
            self.token = self.get_token()
            return self.post(*args, **kwargs)
        return response

    def get_token(self) -> str:
        return "eyJraWQiOiIxZDE1NjJiOS04ODM1LTQ1OGYtODAyMy1mOGU0Nzk0YzIwYTEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4ZTgxMGU5ZS1kNDA5LTQ2ZjItYTE4YS01YzM4MmNlZWFjY2IiLCJhdWQiOiJjb20uY2FyZWVtLmludGVybmFsIiwiYXpwIjoiOGU4MTBlOWUtZDQwOS00NmYyLWExOGEtNWMzODJjZWVhY2NiIiwic2NvcGUiOiJwb3MiLCJpc3MiOiJodHRwczpcL1wvaWRlbnRpdHkucWEuY2FyZWVtLWVuZ2luZWVyaW5nLmNvbVwvIiwiZXhwIjoxNjEyMzg5ODIwLCJpYXQiOjE2MTIzMDM0MjAsImp0aSI6ImU4NDQwNTA4LWRjNzAtNDdiYS05M2I2LTI4OGU1MDNjOTVhNCJ9.gxgQILlcfNeAx1X4cFBOdzBLU6ddRgKT6vvvoVqwLFHuFTdwXuKxUfnPNs7BqjdQ_KGBKu4PA2ool7sZzVNQy3No4ezSCiCA4m-Dv3JXE7dIgBFiubPs-7i_pnFVRVYwmKQF1Aq013Jiqpfa1RuYPe-nDsgiseh9qCH_L8AKrqru55TwFPM1y285IHOiVobMvHpCxZeTQagJbOh2GHW88fAlAJ5zduUtntv6H_mLZ1HlSxdbbzQgxywxQ8gCu1ah2G1n_G8bDLJVKysy2x3E94xh8z7m-RUuV2_4dsU0eCaAgwOsL5x7AviwNCA55nTQHjc1aBRazSi9whemYiMGvQ"
        payload = {
            'grant_type': 'client_credentials',
            'scope': 'pos',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(self.identity_token_api, data=payload)
        token_response = CareemIdentityToken(**response.json())
        return token_response.access_token
