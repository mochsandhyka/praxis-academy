from flask import Flask,render_template,request,redirect,url_for

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

@app.route("/porto", methods=["POST","GET"])
def porto():
    if request.method == "POST":
        porto = request.form["inputNamaDepan"]
        return redirect(url_for("afterPorto",porto=afterPorto))
    else:
        return render_template("port.html")

@app.route("/<porto>")
def afterPorto(porto):
    return "{porto}"
