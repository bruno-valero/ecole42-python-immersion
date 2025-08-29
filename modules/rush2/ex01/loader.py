from sqlalchemy import create_engine, Engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import sys

import csv
import json

Base: DeclarativeBase = declarative_base()


class Database:
    __instance: "Database" = None
    engine: Engine
    session_local: sessionmaker#type:ignore

    def __new__(cls, db_url: str = "loader.sqlite") -> "Database":
        if cls.__instance == None:
            cls.__instance = super(Database, cls).__new__(cls)
            cls.__instance.engine = create_engine(f"sqlite:///{db_url}", echo=False)
            cls.__instance.session_local = sessionmaker(bind=cls.__instance.engine)
            Base.metadata.create_all(bind=cls.__instance.engine)
        return cls.__instance

    def get_session(self) -> Session:
        return self.session_local()#type:ignore


class Accounts(Base):#type:ignore
    __tablename__ = "accounts"

    numero = Column(String, primary_key=True)
    titular = Column(String)
    saldo = Column(Float)
    limite = Column(Integer)
    data_abertura = Column(DateTime)

    def from_list(lst: list[dict]):#type:ignore
        return [Accounts(**i) for i in lst]


class ReadFile:
    def __init__(self, path: str) -> None:
        if not path:
            raise FileNotFoundError("Please Insert a valid path")
        self.path: str = path
        self.content: list[dict] = []#type:ignore

    def remove_duplicateds(self, lst: list[dict]) -> list[dict]:#type:ignore
        duplicateds: set[str] = set()
        results: list[dict] = []#type:ignore
        for acc in lst:
            if acc["numero"] not in duplicateds:
                results.append(
                    {
                        **acc,
                        "saldo": float(acc["saldo"]),
                        "data_abertura": datetime.strptime(
                            acc["data_abertura"], "%Y-%m-%d"
                        ),
                        "limite": int(acc["limite"]),
                    }
                )
            duplicateds.add(acc["numero"])
        return results

    def read_csv_file(self):#type:ignore
        with open(self.path) as file:
            reader = csv.DictReader(file)
            return self.remove_duplicateds(reader)#type:ignore

    def read_json_file(self):#type:ignore
        data = [] #type:ignore
        with open(self.path) as file:
            for line in file:
                data.append(json.loads(line))
        return self.remove_duplicateds(data)


class InvalidFile(Exception):
    def __init__(self):#type:ignore
        super().__init__("Error: Invalid file")#type:ignore


def main(file_path: str) -> int:
    db = Database()
    session = db.get_session()
    data: list[dict] = []#type:ignore
    if file_path.endswith(".csv"):
        data = ReadFile(file_path).read_csv_file()#type:ignore
    elif file_path.endswith(".jsonl"):
        data = ReadFile(file_path).read_json_file()#type:ignore
    else:
        raise InvalidFile()#type:ignore
    accs = Accounts.from_list(data)
    current_data = session.query(Accounts).all()
    session.add_all(accs)
    session.commit()
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            result = main(sys.argv[1])
            sys.exit(result)
        except FileNotFoundError:
            print("Error: Please Insert a valid path")
            sys.exit(1)
        except IsADirectoryError:
            print("Error: Please Insert a valid file")
            sys.exit(1)
        except InvalidFile:
            print("Error: Invalid file")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {type(e).__name__}")
            sys.exit(1)
    else:
        print("Error: Please Insert a valid path")
    sys.exit(1)
