from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def about():
    return render_template("register.html")

@app.route("/syarat")
def syarat():
    return render_template("syarat.html")