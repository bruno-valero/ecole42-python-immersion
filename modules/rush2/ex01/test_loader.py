import pytest
from loader import Database, ReadFile, InvalidFile, Accounts


# @pytest.mark.parametrize("", [


# ])
def test_insert_and_duplicates() -> None:
    file_path: str = "accounts.csv"
    db = Database("test.sqlite")
    session = db.get_session()
    data: list[dict] = [] #type:ignore
    if file_path.endswith(".csv"):
        data = ReadFile(file_path).read_csv_file()
    elif file_path.endswith(".jsonl"):
        data = ReadFile(file_path).read_json_file()
    else:
        raise InvalidFile() #type:ignore
    accs = Accounts.from_list(data)
    session.add_all(accs)
    session.commit()

    assert len(session.query(Accounts).all()) > 0
