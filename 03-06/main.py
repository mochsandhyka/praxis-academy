from flask import Flask, render_template,request,redirect,url_for,session
from flask_login import LoginManager
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

class Kategori(db.Entity):
    pk_kategori = PrimaryKey(int, auto=True)
    kategori = Required(str, unique=True)
    buku = Set('Buku')

class Pengarang(db.Entity):
    pk_pengarang = PrimaryKey(int, auto=True)
    nama_pengarang = Required(str, unique=True)
    buku = Set('Buku')

class Penerbit(db.Entity):
    pk_penerbit = PrimaryKey(int, auto=True)
    nama_penerbit = Required(str, unique=True)
    buku = Set('Buku')

class Buku(db.Entity):
    pk_buku = PrimaryKey(int, auto=True)
    stok = Required(int)
    judul_buku = Required(str)
    # detailPeminjaman = Set('DetailPeminjaman')
    kategori = Required(Kategori,column='fk_kategori')
    pengarang = Required(Pengarang,column='fk_pengarang')
    penerbit = Required(Penerbit,column='fk_penerbit')
    peminjaman = Set('Peminjaman')

class Peminjaman(db.Entity):
    pk_peminjaman = PrimaryKey(int, auto=True)
    tanggal_peminjaman = Required(datetime)
    tanggal_kembali = Required(datetime)
    anggota = Required(Anggota,column='fk_anggota')
    admin = Optional(Admin,column='fk_admin')
    buku = Required(Buku, column='fk_buku')

# class DetailPeminjaman(db.Entity):
#     pk_peminjaman = PrimaryKey(int, auto=True)
#     buku = Required(Buku,column='fk_buku')

db.bind(provider="postgres",user="sandika", password="460446", host="localhost", database="perpustakaan")
db.generate_mapping(create_tables=True)
Pony(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'Login'

# @login_manager.user_loader
# def load_user(user_id):
#     return db.Email.get(pk_admin = user_id)


def getForm(a):
    b = request.form.get(a)
    return b

def selectKategori():
    a = db.execute(f"select *from kategori")
    return a

def selectPeminjaman():
    a = db.execute(f"select *from peminjaman")
    return a

def selectAdmin():
    a = db.execute(f"select *from admin")
    return a

def selectAnggota():
    a = db.execute(f"select *from anggota")
    return a

def selectBuku():
    a = db.execute(f"select *from buku")
    return a

def selectPengarang():
    a = db.execute(f"select *from pengarang")
    return a

def selectPenerbit():
    a = db.execute(f"select *from penerbit")
    return a

################################### HOME ###################################

@app.route("/login")
#@login_required
def vLogin():
    return render_template("Login.html")

@app.route("/login",methods=['POST'])
def Login():
    email = getForm('email')
    password = getForm('password')
    a = db.execute(f"select *from anggota where email_anggota = '{email}' and password = '{password}'")
   

    return render_template("Home.html",a=a)

################################### BUKU ###################################

@app.route("/buku")
def vBuku():
    viewDataBuku = selectBuku()
    viewKategori = selectKategori()
    viewPenerbit = selectPenerbit()
    viewPengarang = selectPengarang()
    return render_template("Buku.html", viewDataBuku = viewDataBuku, viewKategori = viewKategori,viewPenerbit = viewPenerbit, viewPengarang=viewPengarang)

@app.route("/buku",methods=['POST'])
def createBuku():
    judulBuku = getForm('nama_buku')
    stok = getForm('jumlah_buku')
    kategori = getForm('kategori')
    pengarang = getForm('pengarang')
    penerbit = getForm('penerbit')
    db.execute(f"insert into buku(stok,judul_buku,fk_kategori,fk_pengarang,fk_penerbit) values('{stok}','{judulBuku}','{kategori}','{pengarang}','{penerbit}')")
    return redirect(url_for("vBuku"))

@app.route("/deleteBuku/<id>")
def deleteBuku(id):
    db.execute(f"delete from buku where pk_buku = {id}")
    return redirect(url_for("vBuku"))

@app.route("/updateBuku/<id>")
def viewUpdateBuku(id):
    viewDataBuku = selectBuku()
    viewKategori = selectKategori()
    viewPenerbit = selectPenerbit()
    viewPengarang = selectPengarang()
    viewDataBukuById = db.execute(f"select *from buku where pk_buku = {id}")
    return render_template("UpdateBuku.html", data = viewDataBukuById,viewKategori=viewKategori,viewPenerbit=viewPenerbit,viewPengarang=viewPengarang)

@app.route("/updateBuku/<id>", methods=['POST'])
def updateBuku(id):
    judulBuku = getForm('nama_buku')
    stok = getForm('jumlah_buku')
    kategori = getForm('kategori')
    pengarang = getForm('pengarang')
    penerbit = getForm('penerbit')
    db.execute(f"update buku set judul_buku = '{judulBuku}',stok = {stok},fk_kategori = '{kategori}',fk_pengarang = '{pengarang}', fk_penerbit = '{penerbit}' where pk_buku = {id}")
    return redirect(url_for("vBuku"))


################################### KATEGORI ###################################


@app.route("/kategori")
def vKategori():
    viewDataKategori = selectKategori()
    return render_template("Kategori.html", data = viewDataKategori)

@app.route("/kategori",methods=['POST'])
def createKategori():
    kategori = getForm('kategori')
    db.execute(f"insert into kategori(kategori) values('{kategori}')")
    return redirect(url_for("vKategori"))

@app.route("/deleteKategori/<id>")
def deleteKategori(id):
    db.execute(f"delete from kategori where pk_kategori = {id}")
    return redirect(url_for("vKategori"))

@app.route("/updateKategori/<id>")
def viewUpdateKategori(id):
    viewDataKategoriById = db.execute(f"select *from kategori where pk_kategori = {id}")
    return render_template("UpdateKategori.html", data = viewDataKategoriById)

@app.route("/updateKategori/<id>", methods=['POST'])
def updateKategori(id):
    kategori = getForm('kategori')
    db.execute(f"update kategori set kategori = '{kategori}' where pk_kategori = {id} ")
    return redirect(url_for("vKategori"))

################################### PENERBIT ###################################

@app.route("/penerbit")
def vPenerbit():
    viewDataPenerbit = selectPenerbit()
    return render_template("Penerbit.html",viewDataPenerbit = viewDataPenerbit)

@app.route("/penerbit",methods=['POST'])
def createPenerbit():
    namaPenerbit = getForm('namaPenerbit')
    db.execute(f"insert into penerbit(nama_penerbit) values('{namaPenerbit}') ")
    return redirect(url_for("vPenerbit"))

@app.route("/deletePenerbit/<id>")
def deletePenerbit(id):
    db.execute(f"delete from penerbit where pk_penerbit = {id}")
    return redirect(url_for("vPenerbit"))

@app.route("/updatePenerbit/<id>")
def viewUpdatePenerbit(id):
    viewDataPenerbitById = db.execute(f"select *from penerbit where pk_penerbit = {id}")
    return render_template("UpdatePenerbit.html", viewDataPenerbitById = viewDataPenerbitById)

@app.route("/updatePenerbit/<id>",methods=['POST'])
def updatePenerbit(id):
    namaPenerbit = getForm('namaPenerbit')
    db.execute(f"update penerbit set nama_penerbit = '{namaPenerbit}' where pk_penerbit = {id}")
    return redirect(url_for("vPenerbit"))


################################### PENGARANG ###################################

@app.route("/pengarang")
def vPengarang():
    viewDataPengarang = selectPengarang()
    return render_template("Pengarang.html",viewDataPengarang = viewDataPengarang)

@app.route("/pengarang",methods=['POST'])
def createPengarang():
    namaPengarang = getForm('namaPengarang')
    db.execute(f"insert into pengarang(nama_pengarang) values('{namaPengarang}') ")
    return redirect(url_for("vPengarang"))

@app.route("/deletePengarang/<id>")
def deletePengarang(id):
    db.execute(f"delete from pengarang where pk_pengarang = {id}")
    return redirect(url_for("vPengarang"))

@app.route("/updatePengarang/<id>")
def viewDataPengarang(id):
    viewDataPengarangById = db.execute(f"select *from pengarang where pk_pengarang = {id}")
    return render_template("UpdatePengarang.html", viewDataPengarangById = viewDataPengarangById)

@app.route("/updatePengarang/<id>",methods=['POST'])
def updatePengarang(id):
    namaPengarang = getForm('namaPengarang')
    db.execute(f"update pengarang set nama_pengarang = '{namaPengarang}' where pk_pengarang = {id}")
    return redirect(url_for("vPengarang"))

################################### ANGGOTA ###################################

@app.route("/anggota")
def vAnggota():
    viewDataAnggota = selectAnggota()
    return render_template("Anggota.html",viewDataAnggota = viewDataAnggota)

@app.route("/anggota",methods=['POST'])
def createAnggota():
    emailAnggota = getForm('emailAnggota')
    namaAnggota = getForm('namaAnggota')
    jkAnggota = getForm('jkAnggota')
    password = getForm('password')
    db.execute(f"insert into anggota(email_anggota,nama_anggota,jk_anggota,password) values('{emailAnggota}','{namaAnggota}','{jkAnggota}','{password}')")
    return redirect(url_for("vAnggota"))

@app.route("/deleteAnggota/<id>")
def deleteAnggota(id):
    db.execute(f"delete from anggota where pk_anggota = {id}")
    return redirect(url_for("vAnggota"))

@app.route("/updateAnggota/<id>")
def viewUpdateAnggota(id):
    viewDataAnggotaById = db.execute(f"select *from anggota where pk_anggota = {id}")
    return render_template("UpdateAnggota.html",viewDataAnggotaById = viewDataAnggotaById)

@app.route("/updateAnggota/<id>",methods=['POST'])
def updateAnggota(id):
    emailAnggota = getForm('emailAnggota')
    namaAnggota = getForm('namaAnggota')
    jkAnggota = getForm('jkAnggota')
    password = getForm('password')
    db.execute(f"update anggota set email_anggota = '{emailAnggota}', nama_anggota = '{namaAnggota}', jk_anggota = '{jkAnggota}', password = '{password}' where pk_anggota = {id}")
    return redirect(url_for("vAnggota"))




################################### ADMIN ###################################

@app.route("/admin")
def vAdmin():
    viewDataAdmin = selectAdmin()
    return render_template("Admin.html",viewDataAdmin = viewDataAdmin)

@app.route("/admin",methods=['POST'])
def createAdmin():
    emailAdmin = getForm('emailAdmin')
    namaAdmin = getForm('namaAdmin')
    jkAdmin = getForm('jkAdmin')
    password = getForm('password')
    db.execute(f"insert into admin(email_admin,nama_admin,jk_admin,password) values('{emailAdmin}','{namaAdmin}','{jkAdmin}','{password}')")
    return redirect(url_for("vAdmin"))

@app.route("/deleteAdmin/<id>")
def deleteAdmin(id):
    db.execute(f"delete from admin where pk_admin = {id}")
    return redirect(url_for("vAdmin"))

@app.route("/updateAdmin/<id>")
def viewUpdateAdmin(id):
    viewDataAdminById = db.execute(f"select *from admin where pk_admin = {id}")
    return render_template("UpdateAdmin.html",viewDataAdminById = viewDataAdminById)

@app.route("/updateAdmin/<id>",methods=['POST'])
def updateAdmin(id):
    emailAdmin = getForm('emailAdmin')
    namaAdmin = getForm('namaAdmin')
    jkAdmin = getForm('jkAdmin')
    password = getForm('password')
    db.execute(f"update admin set email_admin = '{emailAdmin}', nama_admin = '{namaAdmin}', jk_admin = '{jkAdmin}', password = '{password}' where pk_admin = {id}")
    return redirect(url_for("vAdmin"))



 
#     tanggal_peminjaman = Required(datetime)
#     tanggal_kembali = Required(datetime)
#     anggota = Required(Anggota,column='fk_anggota')
#     admin = Required(Admin,column='fk_admin')
#     buku = Required(Buku, column='fk_buku')

@app.route("/peminjamanAnggota")
def vPeminjaman():
    viewBuku = db.execute(f"select *from buku where stok > 0")
    return render_template("Peminjaman.html",viewBuku=viewBuku)
 

@app.route("/peminjamanAnggota/<id>",methods = ['POST'])
def createPeminjaman(id):
    tanggalPeminjaman = datetime.now()
    tanggalKembali = datetime.now() #getForm('tanggalKembali')
    anggota = 1 # session anggota
    buku = db.execute(f"select pk_buku from buku where pk_buku = {id}")
    for a in buku:
        buku = a 
    buku = sum(buku)
    print(buku)
    a = db.execute(f"select stok from buku where pk_buku = {id}")
    for a in a:
        a = a
    b = sum(a) 
    if b > 0:
        db.execute(f"insert into peminjaman(tanggal_peminjaman,tanggal_kembali,fk_anggota,fk_buku) values('{tanggalPeminjaman}','{tanggalKembali}',{anggota},{buku})")
        db.execute(f"update buku set stok = (stok - 1) where pk_buku = {id}")
        return redirect(url_for("vPeminjaman"))
    else:
        return redirect(url_for("vPeminjaman"))
    #return render_template("Home.html",a=a)

@app.route("/peminjamanAdmin")
def vPeminjamanAdmin():
    viewPeminjaman = selectPeminjaman()
    return render_template("PeminjamanAdmin.html", viewPeminjaman = viewPeminjaman)

@app.route("/deletePeminjamanAdmin/<id>")
def deletePeminjamanAdmin(id):
    db.execute(f"delete from peminjaman where pk_peminjaman = {id}")
    return redirect(url_for('vPeminjamanAdmin'))

@app.route("/accAdmin/<id>",methods=['POST'])
def accAdmin(id):
    a = 1 #session id admin
    db.execute(f"update peminjaman set fk_admin = {a} where pk_peminjaman = {id}")
    return redirect(url_for('vPeminjamanAdmin'))
    

