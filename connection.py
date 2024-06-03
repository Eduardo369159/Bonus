import os
from sqlalchemy import create_engine,text,insert,Table,MetaData
from sqlalchemy.engine import URL
from dotenv import find_dotenv,load_dotenv
load_dotenv(find_dotenv())

class Db():
    def __init__(self):
        connection_string = {
            'database':os.getenv("database"),
            'drivername':os.getenv("drivername"),
            'host':os.getenv("host"),
            'username':os.getenv("user"),
            'password':os.getenv("password")
        }

        self.metadata = MetaData()

        connection_url = URL.create(**connection_string)

        self.__engine = create_engine(connection_url,future=True)
    def execute(self,query):
        with self.__engine.begin() as conn:
            return conn.execute(text(query)).all()


    def insert(self,query,values):
      with self.__engine.begin() as conn:
          return conn.execute(text(query),values)
      
    def inserir(self,data):
        RB_RELATORIO_BANCOS = Table('tbBonus_teste',self.metadata,autoload_with=self.__engine)
        stmt = insert(RB_RELATORIO_BANCOS).values(data)
        with self.__engine.begin() as conn: 
            conn.execute(stmt)
