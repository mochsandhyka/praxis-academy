from flask import Flask, render_template,request,redirect,url_for
from pony.flask import Pony
from pony.orm import Database,Required

app = Flask(__name__)
db = Database()

class Task(db.Entity):
    taskName = Required(str)
    description = Required(str)


db.bind(provider="postgres", user="sandika", password="460446", host="localhost", database="bebas")
db.generate_mapping(create_tables=True)
Pony(app)

#  insert into task(taskname, description) values ('a','b');

@app.route("/", methods=["POST"])
def create():
    afterPorto = request.form.to_dict(flat=True)
    taskName = afterPorto.values()
    list = []
    for i in taskName:
        list.append(i) 
    db.execute(f"INSERT INTO task(taskname, description) VALUES ('{list[0]}','{list[1]}');")
    return redirect(url_for("index"))
       
@app.route("/")
def index(): 
    query = db.execute("select * from task")
    return render_template("index.html",query=query)

@app.route("/detail/<id>")
def detail(id):
    query = db.execute(f"select taskname,description from task where id = {id}")
    return render_template("detail.html",query=query)

@app.route("/delete/<id>")
def delete(id):
    db.execute(f"delete from task where id = {id}")
    return redirect(url_for("index"))

@app.route("/update/<id>")
def viewUpdate(id):
    query = db.execute(f"select *from task where id = {id}")
    return render_template("update.html",query=query)

@app.route("/update/<id>", methods=["POST"])
def update(id):
    a = request.form.to_dict(flat=True)
    b = a.values()
    list = []
    for i in b:
        list.append(i)
    query = db.execute(f"update task set taskname = '{list[0]}', description = '{list[1]}' where id = id")
    return redirect(url_for("index"))


    