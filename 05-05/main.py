from flask import Flask,request,jsonify
from pony.flask import Pony
from pony.orm import Database,Required,PrimaryKey,Set
from http import HTTPStatus
from flask_jwt_extended import JWTManager,create_access_token,get_current_user,get_jwt_identity
import os,re,hashlib

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]") 
jwt = JWTManager(app)
db = Database()

class User(db.Entity):
    pk_user = PrimaryKey(int,auto = True)
    username = Required(str,unique = True)
    email = Required(str,unique = True)
    password = Required(str)
    name = Required(str)
    gender = Required(str)
    borrowing = Set('Borrowing')


class Admin(db.Entity):
    pk_admin = PrimaryKey(int, auto=True)
    username = Required(str,unique = True)
    email = Required(str, unique=True)
    password = Required(str)
    name = Required(str)
    gender = Required(str)
    borrowing = Set('Borrowing')

class BookTypes(db.Entity):
    pk_book_type = PrimaryKey(int, auto=True)
    types = Required(str, unique=True)
    book = Set('Book')

class Author(db.Entity):
    pk_author = PrimaryKey(int, auto=True)
    author_name = Required(str, unique=True)
    book = Set('Book')

class Publisher(db.Entity):
    pk_publisher = PrimaryKey(int, auto=True)
    publisher_name = Required(str, unique=True)
    book = Set('Book')






db.bind(provider=os.getenv('DB_PROVIDER'),user=os.getenv('DB_USER'),password=os.getenv('DB_PASSWORD'),host=os.getenv("DB_HOST"),database=os.getenv("DB_NAME"))
db.generate_mapping(create_tables=True)
Pony(app)


#REGISTER
@app.route("/auth/register", methods=['POST'])
def register():
    try:
        jsonBody = request.json
        email = jsonBody['email']
        #nani = db.select(f"select username,password,email,name from public.user where email = '{email}' and username='{jsonBody['username']}'")
        
        if jsonBody['username'] == "" or jsonBody['password'] == "" or jsonBody['email'] == "" or jsonBody['name'] =="":
            response ={
                "data": "Bad Request",
                "message": "Ada data yang tidak benar"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif email_regex.match(email):
            hashpass = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
            query = f"insert into public.user(username,password,email,name) values ('{jsonBody['username']}','{hashpass.hexdigest()}','{jsonBody['email']}','{jsonBody['name']}')"
            data = db.execute(query) 
            response  ={
                "data": jsonBody,
                "message": "Data inserted"
            }
            return jsonify(response), HTTPStatus.OK
        else:
            response={
                "data": "bad request",
                "message": "email not valid"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
    except Exception as err:
        response ={
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY

# LOGIN
@app.route("/auth/login",methods=['POST'])
def login():
    try:
        jsonBody = request.json
        hashpass = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
        user = db.select(f"select *from public.user where username = '{jsonBody['username']}' and password = '{hashpass.hexdigest()}'")
        if not user:
            response = {
                "data": "Bad Request",
                "message": "Username/ password salah"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        access_token = create_access_token(identity=user)
        response = {
            "data": f"Token : {access_token}",
            "message": "Berhasil Login"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY
    
@app.route("/listBuku")
def listBuku():
    pass

@app.route("/pinjamBuku")
def pinjamBuku():
    pass
