# @TIME : 2020/4/22 19:42
# @Author : lj
# @file : .py
from sqlalchemy import create_engine,Column ,Integer,VARCHAR,String
from sqlalchemy.ext.declarative import declarative_base



HOSTNAME = '127.0.0.1'
DATABASE = 'flask_demo'
USERNAME = 'root'
PASSWORD = 'root'
PORT = 3306

DB_URL = f'mysql+pymysql://{USERNAME}:{PORT}@{HOSTNAME}:{PASSWORD}/{DATABASE}'

Engine = create_engine(DB_URL)

Base = declarative_base(Engine)

class prfiles(Base):
    __tablename__ ='profiles'

    id = Column(Integer,primary_key=True,autoincrement=True)
    names = Column(String(20))

#映射数据库
Base.metadata.create_all()
