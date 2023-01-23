
#membuat virtual environment
#python3 -m venv venv
#masuk ke . venv/bin/activate
#pip install Flask
from flask import Flask,request,redirect

app = Flask(__name__) 

@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/setting")
def setting():
    return "Welcome to Setting Page"

@app.route("/profile/<names>")
def profile(names):
    return f"Welcome to Profiles Page Mr/Mrs {names}"

@app.route("/profil/<int:id>")
def profileId(id):
    return f"Your profile id is {id}"

@app.route("/query/")
def query():
    query = request.args.get("nama")
    return query 

#redirect
@app.route("/redirect/")
def redirectHome():
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)


