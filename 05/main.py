from flask import Flask, render_template,redirect,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from pony.flask import Pony
from pony.orm import Database,Required
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "a223jun98e23nce2j3ce23"
db =Database()

class User(db.Entity):
    name = Required(str)
    email = Required(str)
    date_added = Required(datetime)

class NameFormer(FlaskForm):
    name = StringField("What's Your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def home():
    return "this is home"

@app.route("/name",methods=['GET','POST'])
def name():
    name = None
    form = NameFormer()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")
    return render_template("name.html", name = name, form = form)