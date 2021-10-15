from app import routesController
import uuid

List = []


def fetch_List() -> dict:
    if List.len() == 0:
        raise Exception("No data was found (List is empty).")
    return List


def fetch_byID(id: int) -> dict:
    if List.len() == 0:
        raise Exception("No data was found (List is empty).")

    for item in List:
        if (item["id"] == id):
            return item

    raise Exception("Item was not found")


def update_ListTask(id: int, text: str, status: int) -> None:
    for item in List:
        if List["id"] == id:
            List["description"] = text
            List["status"] = status
            return

    raise Exception("Item was not found")


def update_ListTask_status(id: int, status: id) -> None:
    for item in List:
        if item["id"] == id:
            List["status"] = status
            return

    raise Exception("Item was not found")


def delete_byID(id: int) -> None:
    for item in List:
        if item["id"] == id:
            List[id].pop()
            return

    raise Exception("Item was not found")


def insert_List(text: str) -> None:
    List.append({
        "id": uuid.uuid1(),
        "description": text,
        "status": 0
    })
