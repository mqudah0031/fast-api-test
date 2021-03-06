from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from db.base import Base


class App(Base):
    __tablename__ = "app"
    id = Column(Integer, Sequence('app_id_seq'), primary_key=True)
    name = Column(String)
    client_id = Column(String)
    client_secret = Column(String)
    redirect_uri = Column(String)

    developer = relationship("user")
