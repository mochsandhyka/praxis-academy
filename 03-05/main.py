from flask import Flask, render_template,request,redirect,url_for
from pony.flask import Pony
from pony.orm import Database,Required

app = Flask(__name__)
db = Database()

class Siswa(db.Entity):
    namaSiswa = Required(str)
    umur = Required(int)
    alamat = Required(str)
    idEkstra = Required(int)

class Ekstra(db.Entity):
    namaEkstra = Required(str)

# class Guru(db.Entity):
#     namaGuru = Required(str)
#     umur = Required(int)
#     idEkstra = Required(int)

    

db.bind(provider="postgres",user="sandika", password="460446", host="localhost", database="sekolah")
db.generate_mapping(create_tables=True)
Pony(app)

@app.route("/")
def home():
    return render_template("index.html")

def rfg(a):
    b = request.form.get(a)
    return b

@app.route("/siswa",methods=["POST"])
def createSiswa():
    nama = rfg('namaSiswa')
    um = rfg('umur')
    al = rfg('alamat')
    ie = rfg('idekstra')
    
    db.execute(f"insert into siswa(namaSiswa,umur,alamat,idekstra) values ('{nama}','{um}','{al}','{ie}')")
    return redirect(url_for("dataSiswa"))

@app.route("/detail/<id>")
def detailSiswa(id):
    viewDataSiswa = db.execute(f"select siswa.namaSiswa,siswa.umur,siswa.alamat,ekstra.namaEkstra from siswa inner join ekstra on siswa.idekstra = ekstra.id where siswa.id = {id}")
    return render_template("detail.html",data = viewDataSiswa)


@app.route("/siswa")
def dataSiswa():
    viewDataSiswa = db.execute(f"Select *from siswa")
    viewDataSiswa2 = db.execute(f"SELECT id, namaekstra from ekstra")
    viewDataSiswa3 = db.execute(f"select siswa.id,siswa.namaSiswa,ekstra.namaekstra from siswa inner join ekstra on siswa.idekstra = ekstra.id")
    
    
    return render_template("siswa.html",data2 = viewDataSiswa2,data = viewDataSiswa,data3 = viewDataSiswa3)

@app.route("/ekstra")
def dataEkstra():
    viewDataEkstra = db.execute(f"SELECT *from ekstra")
    return render_template("ekstra.html",data = viewDataEkstra)

@app.route("/ekstra", methods=["POST"])
def createEkstra():
    nama = rfg('namaEkstra')
    db.execute(f"insert into ekstra(namaekstra) values('{nama}')")
    return redirect(url_for("dataEkstra"))

@app.route("/delete/<id>")
def delete(id):
    db.execute(f"delete from siswa where id = {id}")
    return redirect(url_for('dataSiswa'))








#create table a (id_siswa int ,id_ekstra int , primary key(id_siswa,id_ekstra), foreign key(id_siswa) references siswa(id), foreign key(id_ekstra) references ekstra(id));

    

# @app.route("/siswa", methods=["POST"])
# def insertSiswa():
#     # namasiswa = request.form.get('namasiswa')
#     # umur = request.form.get('umur')
#     # alamat = request.form.get('alamat')
#     afterPorto = request.form.to_dict(flat=True)
#     taskName = afterPorto.values()
#     list = []
#     for i in taskName:
#         list.append(i) 
    
#     db.execute(f"insert into siswa(namasiswa, umur, alamat) values ('{list[0]}','{list[1]}','{list[2]}');")
#     return redirect(url_for("siswa"))
