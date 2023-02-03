from flask import Flask,render_template,request,redirect,url_for
from pony.flask import Pony
from pony.orm import Database,Required

app = Flask(__name__)
db = Database()

class Task(db.Entity):
    task_name = Required(str)
    description = Required(str)
    status = Required(bool)

db.bind(provider="postgres", user="sandika", password="460446", host="localhost", database="task")
db.generate_mapping(create_tables=True)
Pony(app)

def datas():
    data = request.form.to_dict(flat=True)
    task2 = data.values()
    task = []
    for i in task2:
        task.append(i)
    

@app.route("/")
def index():
    query = db.execute("SELECT *FROM task")
    return render_template("todoList.html",taskList=query)

@app.route("/", methods=['POST'])
def create():
    data = request.form.to_dict(flat=True)
    task2 = data.values()
    task = []
    for i in task2:
        task.append(i)
    
    db.execute(f"INSERT INTO task(task_name,description,status) VALUES ('{task[0]}','{task[1]}',False)")
    return redirect(url_for("index"))

@app.route("/delete/<id>")
def delete(id):
    db.execute(f"DELETE from task where id = {id}")
    return redirect(url_for("index"))

@app.route("/update/<id>")
def viewUpdate(id):
    query = db.execute(f"SELECT id,task_name, description, status from task where id = {id}")
    return viewUpdate(id) #render_template("todoList.html", query = query)

@app.route("/update/<id>",methods=["POST"])
def update(id):
    data = request.form.to_dict(flat=True)
    task2 = data.values()
    task = []
    for i in task2:
        task.append(i)
    db.execute(f"update task set task_name = '{task[0]}', description = '{task[1]}',status = {task[2]} where id = id")
    return redirect(url_for("index"))
    

    
