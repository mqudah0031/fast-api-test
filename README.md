# FastAPI
fastapi + uvicorn + sqlalchemy(postgres) + celery + oauth2

## getting started
create a virtual env and activate it
```text
python3 -m venv venv
source venv/bin/activate
```
install requirements
```text
pip install -r requirements.txt
```
create a `.env` file
```text
SECRET=

DB_HOST=postgres
DB_PORT=5432
DB_DB_NAME=fast_api_test
DB_USER=<username>
DB_PASS=<password>

CELERY_BROKER=redis://redis:6378/0
```

build docker
```text
cd fast-api-nuggets-build
docker-compose build
```
then start the containers
```text
docker-compose up
```
makemigrations and migrate
```text
 docker-compose exec server alembic revision  --autogenerate
```
```text
docker-compose exec server alembic upgrade head 
```

## migrations
in order for alembic to automatically generate migrations for a model import it in top of `albemic/env.py`

example: you want to add a new model called `Car`

```python
from auth.models.user import User
+ from car.models.user import Car
from db.base import Base
target_metadata = Base.metadata
```

## Database models
database models are normal python classes inheriting `base` from sqlalchemy.

this project provides a django-like manager for models

example:

```python
from sqlalchemy import Column, String
from db.base import Base
from db.manager import Manager


class User(Base):
    __tablename__ = "user"
    username = Column(String, unique=True)

 +   objects: Manager # <---

    def __repr__(self):
        return f"<User(username={})>".format(self.username)


+ User.objects = Manager(User) # <----

```
you can now use it like this
```python
User.objects.create(...)
User.objects.filter(...)
User.objects.find(....)
```
the manager will handle creating and closing sessions for these actions.

to create a custom method simple inherit the Manger class and use it in the Model.