from flask import request, jsonify
from app import Arr
from app import app


@app.route("/api/v1/todo/<id>", methods=["DELETE"])
def delete(id):
    """[Deletes a certain todo if its ID was found]

    Args:
        id (int): [In order to use it as a reference to a todo item]

    Returns:
        [dictionary]: [The function will return the same list with the deleted todo in the specified ID]
    """
    try:
        Arr.delete_byID(id)
        result = {
            "success": 200,
            "response": "Item was deleted."
        }

    except:
        result = {
            "success": 404,
            "response": str(Exception)
        }

    return jsonify(result)


@app.route("/api/v1/todo/<id>", methods=["PUT"])
def update(id):
    """[Updates a certain todo if its ID was found]

    Args:
        id (int): [In order to use it as a reference to a todo item]
    Returns:
        [dictionary]: [The function will return a certain todo with the modified values in the specified ID]
    """

    try:
        data = request.get_json()
        Arr.update_ListTask(id, data["description"], data["status"])
        result = {
            "success": 200,
            "response": "Item was updated successfully"
        }

    except:
        result = {
            "success": 404,
            "response": str(Exception)
        }

    return jsonify(result)


@app.route("/api/v1/todo/<id>", methods=["PATCH"])
def update_status(id):
    """[Update the status of a certain todo if its ID was found]

    Args:
       id (int): [In order to use it as a reference to a todo item]

    Returns:
        [dictionary]: [The function will return a certain todo with modified status in the specified ID]
    """
    try:
        data = request.get_json()
        Arr.update_ListTask_status(id, data["status"])
        result = {
            "success": 200,
            "response": "Status was modified."
        }

    except:
        result = {
            "success": 404,
            "response": str(Exception)
        }

    return jsonify(result)


@app.route("/api/v1/todo/", methods=['POST'])
def create():
    """[Inserts a description into a todo in addition to a generated id, and a constant initial status(0)]

    Returns:
        [dictionary]: [The function will return the inserted todo]
    """
    data = request.get_json()
    Arr.insert_List(data["description"])
    result = {
        'success': 200,
        'response': 'Item was inserted'
    }

    return jsonify(result)


@app.route("/api/v1/todo/", methods=["GET"])
def getAllTODOs():
    """[Returns the entire list of todos]

    Returns:
        [dictionary]: [The function will return the entire list]
    """
    try:
        result = Arr.fetch_List()
        items = {
            "status": 200,
            "response": result
        }
        return jsonify(items)

    except Exception:
        items = {
            'status': 404,
            "response": str(Exception)
        }


@app.route("/api/v1/todo/<id>", methods=["GET"])
def getTODObyID(id):
    """[summary]

    Args:
        id (int): [In order to use it as a reference to a todo item]

    Returns:
        [dictionary]: [The function will return the todo that has this certain ID]
    """
    try:
        result = Arr.fetch_byID(id)
        items = {
            "status": 200,
            "response": result
        }

    except Exception:
        items = {
            'status': 404,
            "response": str(Exception)
        }

    return jsonify(items)