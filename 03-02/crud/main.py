from flask import Flask, flash, redirect, render_template, \
     request, url_for
from pony.flask import Pony
# from flask_login import UserMixin,login_user, LoginManager, login_required,logout_user,current_user
from pony.orm import Database,Required

app = Flask(__name__)
db = Database()

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# app.secret_key = b'7e7793e4f406d22ada240fb18e261c8e817a2223b054d72c9c268372ec6fa254'

# class Task(db.Entity,UserMixin):
#     taskName = Required(str)
#     description = Required(str)

def task():
    a = db.execute(f"select *from task")
    return a

db.bind(provider="postgres", user="sandika", password="460446", host="localhost", database="bebas")
db.generate_mapping(create_tables=True)
Pony(app)

# @login_manager.user_loader
# def load_user(id):
#     a = Task.get(id)
#     return Task.get(id)


# @login_manager.unauthorized_handler
# def unauthorized_callback():             
#        return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#                 request.form['password'] != 'secret':
#             error = 'Invalid credentials'
#         else:
#             flash('You were successfully logged in')
#             user = login_user("admin")
            
            
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)

@app.route("/")
def index():
    query = db.execute("select * from task")
    return render_template("index.html",query=query)


@app.route("/", methods=["POST"])
def create():
    # afterPorto = request.form.to_dict(flat=True)
    # taskName = afterPorto.values()
    # list = []
    # for i in taskName:
    #     list.append(i) 
    taskName = request.form.get('taskName')
    description = request.form.get('description')
    db.execute(f"INSERT INTO task(taskname, description) VALUES ('{taskName}','{description}');")
    return redirect(url_for("index"))
        
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
    query = db.execute(f"update task set taskname = '{list[0]}', description = '{list[1]}' where id = {id}")
    return redirect(url_for("index"))


    