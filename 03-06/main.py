from flask import Flask, render_template,request,redirect,url_for
from datetime import datetime
from pony.flask import Pony
from pony.orm import *

app = Flask(__name__)
db = Database()


class Admin(db.Entity):
    pk_admin = PrimaryKey(int, auto=True)
    email_admin = Required(str, unique=True)
    nama_admin = Required(str)
    jk_admin = Required(str)
    password = Required(str)
    peminjaman = Set('Peminjaman')

class Anggota(db.Entity):
    pk_anggota = PrimaryKey(int, auto=True)
    email_anggota = Required(str, unique=True)
    nama_anggota = Required(str)
    jk_anggota = Required(str)
    password = Required(str)
    peminjaman = Set('Peminjaman')

class Peminjaman(db.Entity):
    pk_peminjaman = PrimaryKey(int, auto=True)
    tanggal_peminjaman = Required(datetime)
    tanggal_kembali = Required(datetime)
    anggota = Required(Anggota,column='fk_anggota')
    admin = Required(Admin,column='fk_admin')

class Buku(db.Entity):
    pk_buku = PrimaryKey(int, auto=True)
    stok = Required(int)
    judul_buku = Required(str)
    detailPeminjaman = Set('DetailPeminjaman')

class DetailPeminjaman(db.Entity):
    pk_peminjaman = PrimaryKey(int, auto=True)
    buku = Required(Buku,column='fk_buku')

db.bind(provider="postgres",user="sandika", password="460446", host="localhost", database="perpustakaan")
db.generate_mapping(create_tables=True)
Pony(app)

#     id_admin
#     email_admin 
#     nama_admin
#     jk_admin 
#     password 

def getForm(a):
    b = request.form.get(a)
    return b

@app.route("/")
def Home():
    return "welcome"

@app.route("/anggota")
def Anggota():
    return "Anggota"

@app.route("/buku")
def Buku():
    viewDataBuku = db.execute(f"select *from buku")
    return render_template("Buku.html", data = viewDataBuku)

@app.route("/buku",methods=['POST'])
def createBuku():
    judulBuku = getForm('nama_buku')
    stok = getForm('jumlah_buku')
    db.execute(f"insert into buku(stok,judul_buku) values('{stok}','{judulBuku}')")
    return redirect(url_for("Buku"))

@app.route("/deleteBuku/<id>")
def deleteBuku(id):
    db.execute(f"delete from buku where pk_buku = {id}")
    return redirect(url_for("Buku"))

@app.route("/updateBuku/<id>")
def viewUpdateBuku(id):
    viewDataBukuById = db.execute(f"select *from buku where pk_buku = {id}")
    return render_template("UpdateBuku.html", data = viewDataBukuById)

@app.route("/updateBuku/<id>", methods=['POST'])
def updateBuku(id):
    judulBuku = getForm('nama_buku')
    stok = getForm('jumlah_buku')
    db.execute(f"update buku set judul_buku = '{judulBuku}',stok = {stok} where pk_buku = {id}")
    return redirect(url_for("Buku"))

@app.route("/admin")
def Admin():
    return "Admin"







