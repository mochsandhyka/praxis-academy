
#membuat virtual environment
#python3 -m venv venv
#masuk ke . venv/bin/activate
#pip install Flask
from flask import Flask,request,redirect,url_for,render_template

listHewan = ["Ayam","Kelinci","Kuda"]

app = Flask(__name__) 

@app.route("/")
def home():
    return render_template("index.html", content=listHewan)

@app.route("/setting")
def setting():
    return "Welcome to Setting Page"

@app.route("/profile/<names>")
def profile(names):
    return render_template("index2.html",content=names)


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
    return redirect(url_for("home"))


#source venv/bin/activate
#export FLASK_APP=main.py
#flask run
#if __name__ == '__main__':
#    app.run(debug=True)