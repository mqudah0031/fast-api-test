## PyCareem - python sdk for careemnow api.

api documentation: https://docs.careemnow.com/

**features**
-  automatically refreshes the token.
-  well-structured, all objects and methods are structured in a way that makes sense for the developer. 
-  support for python types for a better development experience.
## Usage

```python
from pycareem.careem import Careem

# if you dont pass the token it will automatically generate one.
# but its better to save it the first time because requesting a token everytime
# can result in getting rate limited or even worse, get your ip banned
# which requires manual approval from careem to get unbanned
careem = Careem('<client_id>', '<client_secret>')
brand = careem.brands.list().data[0]
branch = brand.branches.list().data[0]
branch.update("POSRocket, Amman")
```

now let's explain this, careem offers different services, and you can access these service by selecting them from the
CareemClient, or a service (nested services)

```python
careem.brands  # <-
careem.brands.get(1).branches # <- nested service
careem.brands.get(1).branches.get(123).catalogs # <- nested service
```

usually each service has four main functions: `list` `get` `create` `delete`

---
`list`  takes no parameters, and returns a [Pagination](#pagination) object.

`get`  gets an object by id, and returns the suitable CareemObject 
eg: [CareemBrandResponse](#CareemBrandResponse)
, [CareemBranchResponse](#CareemBranchResponse)
---
# Objects

## Pagination

a python object that contains data(list) and few methods, usually returned from `.list`

```
Pagination.data # : List of the suitable CareemObject
Pagination.next() # : a new pagination object containing the new page
Pagination.prev() # : a new pagination object containing the previous page
```

## CareemBrandResponse

a python object with brand data and few methods.

fields:

```
id: int
name: str
created_at: str
updated_at: str
branches: Any
```

```
CareemBrandResponse.id # get the id
CareemBrandResponse.delete() # deletes the brand
CareemBrandResponse.update("new name") # updates the name
```

## CareemBranchResponse

a python object with branch data and few methods.

fields:

```
id: str
name: str
brand_id: str
state: str
created_at: str
updated_at: str
```

```
CareemBranchResponse.id # get the id
CareemBranchResponse.delete() # deletes the branch
CareemBranchResponse.update("new name") # updates the name: returns a new Object
```