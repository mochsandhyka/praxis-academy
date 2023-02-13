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
        "message": "data found"
    }
    return jsonify(response), HTTPStatus.OK

# @app.route("/")
# def view():
#     try:
#         data = []
#         for i in db.execute("select *from tasklist"):
#             data.append({
#                 "id": i[0],
#                 "task": i[1],
#                 "description": i[2]
#             })
#         response = {
#             "data": data,
#             "message": "ok"
#         }
#         return jsonify(response), HTTPStatus.ok

#     except Exception as response:
#         response = {
#             "data": "bad",
#             "message": "bad gateway"
#         }
#         return jsonify(response),HTTPStatus.BAD_GATEWAY
   

@app.route("/",methods=["POST"])
def create():
    bodyJson = request.json
    queryInsert = f"insert into tasklist(task, description) values('{bodyJson['task']}','{bodyJson['description']}')"
    data = db.execute(queryInsert)
    response = {
        "data": "Created",
        "message": "Data inserted"
    }
    return jsonify(response), HTTPStatus.CREATED

@app.route("/delete/<id>",methods=['DELETE'])
def delete(id):
    try:
        selectById = (f"select id from tasklist where id = {id}")
        data = []
        for i in db.execute(selectById):
            data.append({
                "id": i[0]
            })
        if not data:
            response = {
                "data": "no data",
                "message": "bad request"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        else:
            deleteById = (f"delete from tasklist where id = {id}")
            db.execute(deleteById) 
            response = {
            "data": "delete tasklist",
            "message": "delete success"
        } 
        return jsonify(response), HTTPStatus.ACCEPTED

    except Exception as respError:
        response={
            "data": str(respError),
            "message": "bad gateway"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY
 

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

@app.route("/detail/<id>")
def detail(id):
    try:
        querySelectById = db.execute(f"select task,description from tasklist where id = {id}")
        data = []
        for i in querySelectById:
            data.append({
                "task": i[0],
                "description": i[1]
            })

        if not data:
            respon = {
                "data": "no data",
                "message": "bad"
            }
            return jsonify(respon), HTTPStatus.BAD_REQUEST
        respon = {
            "data": data[0],
            "message": "data is found"
        }
        return jsonify(respon),HTTPStatus.OK
        
    except Exception as respError:
        respon = {
            "data": str(respError),
            "message": "bad gateway"
        }
        return jsonify(respon),HTTPStatus.BAD_GATEWAY


