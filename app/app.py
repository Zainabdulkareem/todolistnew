from flask import Flask, request, jsonify, render_template
from app.main import (
    create_todo,
    get_all_todos,
    get_todo_by_id,
    update_todo,
    delete_todo
)

app = Flask(__name__)


# ✅ GET all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(get_all_todos())


# ✅ GET one todo
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_one(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        return {"error": "Not found"}, 404
    return jsonify(todo)


# ✅ CREATE todo
@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data.get("task")

    if not task:
        return {"error": "Task is required"}, 400

    todo_id = create_todo(task)
    return {"message": "Created", "id": todo_id}, 201


# ✅ UPDATE todo
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def edit_todo(todo_id):
    data = request.get_json()
    task = data.get("task")

    updated = update_todo(todo_id, task)

    if not updated:
        return {"error": "Not found"}, 404

    return {"message": "Updated"}


# ✅ DELETE todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def remove_todo(todo_id):
    deleted = delete_todo(todo_id)

    if not deleted:
        return {"error": "Not found"}, 404

    return {"message": "Deleted"}

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)