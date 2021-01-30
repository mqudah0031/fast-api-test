from ..utils import verify_password
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import Session
from db import engine
from db.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    @staticmethod
    def authenticate(username: str, password: str):
        session = Session(bind=engine)
        user = session.query(User).filter_by(username=username).first()
        if not user:
            return False
        if not verify_password(plain_password=password, hashed_password=user.hashed_password):
            return False
        session.close()
        return user

    @staticmethod
    def create(**kwargs):
        session = Session(bind=engine)
        user = User(**kwargs)
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return user

    @staticmethod
    def filter(**kwargs):
        session = Session(bind=engine)
        user = session.query(User).filter_by(**kwargs).first()
        session.close()
        return user

    def __repr__(self):
        return "<User(id={}, username={})>".format(self.id, self.username)
