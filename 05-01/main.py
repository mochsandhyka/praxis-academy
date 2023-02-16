from flask import Flask,jsonify,request
from pony.flask import Pony
from pony.orm import Database,Required
from http import HTTPStatus
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required,JWTManager
import os
import hashlib

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

db = Database()

#class User(db.Entity):
 #   username = Required(str,unique = True)
  #  password = Required(str)

db.bind(provider = os.getenv('DB_PROVIDER'), user = os.getenv('DB_USERNAME'), password = os.getenv('DB_PASSWORD'), host = os.getenv('DB_HOST'), database = os.getenv('DB_NAME'))
db.generate_mapping(create_tables=True)
Pony(app)

@app.route("/auth/login", methods=['POST'])
def login():
    try:
        jsonBody = request.json
        hashpassword = hashlib.md5((jsonBody['password']+ os.getenv("SALT_PASSWORD")).encode())
        user = db.select(f"select username from public.user where username = '{jsonBody['username']}' and password = '{hashpassword.hexdigest()}'")
        if not user:
            response = {
                "data": "Bad Request",
                "message": "Please check again"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST

        access_token = create_access_token(identity=user)
        return jsonify(access_token = access_token)
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY



@app.route("/auth/register", methods=['POST'])
def register():
    try:
        jsonBody = request.json
        if jsonBody['username'] == "" or jsonBody['password'] == "":
            response = {
                "data": "bad",
                "message": "username/password required"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST

        hashpassword = hashlib.md5((jsonBody['password']+ os.getenv("SALT_PASSWORD")).encode())
        query = f"insert into public.user(username,password) values('{jsonBody['username']}','{hashpassword.hexdigest()}')"
        data = db.execute(query)
        response = {
            "data": "data",
            "message": "Data inserted"
        }
        return jsonify(response),HTTPStatus.CREATED
    except Exception as err:
        response = {
            "data": str(err),
            "message": "bad"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY

@app.route("/private")
@jwt_required()
def private():
    currentUser = get_jwt_identity()