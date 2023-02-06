from flask import Flask
from pony.orm import *

app = Flask(__name__)
db = Database()

class Admin(db.Entity)
