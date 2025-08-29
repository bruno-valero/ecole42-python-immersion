from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

Base: DeclarativeBase = declarative_base()

class Database:
    __instance: "Database" = None
    engine: Engine
    session_local: sessionmaker

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(Database, cls).__new__(cls)
            cls.__instance.engine = create_engine('sqlite:///movielist.sqlite', echo=False)
            cls.__instance.session_local = sessionmaker(bind=cls.__instance.engine)
            Base.metadata.create_all(bind=cls.__instance.engine)
        return cls.__instance
    
    def get_session(self) -> Session:
        return self.session_local()