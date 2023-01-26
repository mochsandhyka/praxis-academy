import os
from flask import Flask,render_template,request,redirect,url_for,flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "path/uploads"
ALLOWED_EXTENSION = {"jpg","png"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

listKota = ["Malang","Yogyakarta"]

def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSION

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/porto", methods=["POST","GET"])
def porto():
    if request.method == "POST":
        # if "file" not in request.files:
        #     flash("No file part")
        #     return redirect(request.url)
        # file = request.files["file"]
        # if file.filename == "":
        #     flash("No selected file")
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            afterPorto = request.form.to_dict(flat=True)
            return redirect(url_for("afterPorto", port=afterPorto))
    else:
        return render_template("porto.html",content=listKota)

@app.route("/<port>")
def afterPorto(port):
    return f"{port}"
