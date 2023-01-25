from flask import Flask,render_template

app = Flask(__name__)

listBuku = ["Akutansi Pengantar 1","Akutansi Pengantar 2"]
dictBuku = {"Buku Pelajaran" : {"Judul":["Akutansi Pengantar 1","Akutansi Pengantar 2"]},"Isi":["aaaaaaaaa","bbbbbbbb"]}
a = ["Malang","Yogyakarta"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/portofolio")
def portofolio():
    return  render_template("portofolio.html")