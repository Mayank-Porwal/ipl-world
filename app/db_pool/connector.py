from sqlalchemy import create_engine
from app.db_pool.config import Config


user = Config.USERNAME
password = Config.PWD
db_name = Config.DATABASE


def db_init():
    return create_engine(f'postgresql://{user}:{password}@localhost:5432/{db_name}')
    # return create_engine(f'postgresql://postgres:postgres@localhost:5432/IPL')


db_engine = db_init()

# engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/{db_name}')

# with db_engine.connect() as connection:
#     result = connection.execute(text("Select * from teams"))
#     r = result.fetchall()
#
# print(r)
