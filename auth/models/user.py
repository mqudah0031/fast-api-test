from ..utils import verify_password
from sqlalchemy import Column, Integer, String, Sequence, Boolean
from db.base import Base
from db.manager import Manager


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_superuser = Column(Boolean, default=False)

    objects: Manager

    @staticmethod
    def authenticate(username: str, password: str):
        user = User.objects.find(username=username)
        if not user:
            return False
        if not verify_password(plain_password=password, hashed_password=user.hashed_password):
            return False
        return user

    def __repr__(self):
        return "<User(id={}, username={})>".format(self.id, self.username)


User.objects = Manager(User)
