from sqlalchemy import create_engine
from settings import DATABASE

connection_url = "postgresql://{}:{}@{}:{}/{}".format(DATABASE['USER'], DATABASE['PASSWORD'], DATABASE['HOST'],
                                                      DATABASE['PORT'],
                                                      DATABASE['NAME'])
engine = create_engine(connection_url)
