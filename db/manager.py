from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db import engine
from db.exceptions import DuplicateEntry


def better_exceptions(e):
    if 'psycopg2.errors.UniqueViolation' in str(e):
        raise DuplicateEntry
    raise e


class Manager:
    def __init__(self, model):
        self.model = model

    def create(self, **kwargs):
        """
        inserts a new record with the given kwargs
        :param kwargs:
        :return:
        """
        try:
            session = Session(bind=engine)
            obj = self.model(**kwargs)
            session.add(obj)
            session.commit()
            session.refresh(obj)
            session.close()
            return obj
        except IntegrityError as e:
            better_exceptions(e)

    def filter(self, **kwargs):
        """
        returns a list of records based on the given kwargs
        :param kwargs:
        :return:
        """
        session = Session(bind=engine)
        objs = session.query(self.model).filter_by(**kwargs)
        session.close()
        return objs

    def find(self, **kwargs):
        """
        a copy of .filter that returns the first record
        :param kwargs:
        :return:
        """
        session = Session(bind=engine)
        objs = session.query(self.model).filter_by(**kwargs).first()
        session.close()
        return objs
