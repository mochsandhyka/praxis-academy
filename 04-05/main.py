from flask import Flask,flash,redirect,render_template,request,jsonify
from pony.flask import Pony
from pony.orm import Database,Required
from http import HTTPStatus

app = Flask(__name__)
db = Database()

class TaskList(db.Entity):
    task = Required(str)
    description = Required(str)

db.bind(provider="postgres", user="sandika", password="460446", host="localhost", database="todolist")
db.generate_mapping(create_tables=True)
Pony(app)

@app.route("/")
def view():
    data = []
    for i in db.execute("select *from tasklist"):
        data.append({
            "id": i[0],
            "task": i[1],
            "description": i[2]
        })
    
    response = {
        "data": data,
        "message": "ok"
    }
    return jsonify(response), HTTPStatus.OK

@app.route("/create",methods=["POST"])
def create():
    bodyJson = request.json
    queryInsert = f"insert into tasklist(task, description) values('{bodyJson['task']}','{bodyJson['description']}')"
    db.execute(queryInsert)
    response = {
        "data": "Created",
        "message": "Data inserted"
    }
    return jsonify(response), HTTPStatus.CREATED

@app.route("/delete/<id>",methods=['DELETE'])
def delete(id):
    db.execute(f"delete from tasklist where id = {id}")
    response = {
        "data": "delete tasklist",
        "message": "delete success"
    }
    return jsonify(response), HTTPStatus.ACCEPTED

@app.route("/update/<id>",methods=['PUT'])
def update(id):
    bodyJson = request.json
    queryUpdate = f"update tasklist set task='{bodyJson['task']}' ,description='{bodyJson['description']}' where id = {id}"
    db.execute(queryUpdate)
    response = {
        "data": "Update",
        "message": "Data updated"
    }
    return jsonify(response), HTTPStatus.ACCEPTED


