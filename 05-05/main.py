from flask import Flask,request,jsonify,session
from pony.flask import Pony
from pony.orm import Database,Required,PrimaryKey,Set,Optional
from http import HTTPStatus
from datetime import date
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_current_user,get_jwt_identity
import os,re,hashlib
from flask_cors import CORS
 

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]") 
jwt = JWTManager(app)
db = Database()
CORS(app)

# class User(db.Entity):
#     _table_ = "tbl_user"
#     id_user = PrimaryKey(int,auto = True)
#     username = Required(str,unique = True)
#     email = Required(str,unique = True)
#     password = Required(str)
#     name = Required(str)
#     gender = Required(str)
#     address = Required(str)
#     phone_number = Required(str)
#     borrowedbook = Set('BorrowedBook')
#     returnedbook = Set('ReturnedBook')

# class Admin(db.Entity):
#     _table_ = "tbl_admin"
#     id_admin = PrimaryKey(int, auto=True)
#     username = Required(str,unique = True)
#     email = Required(str, unique=True)
#     password = Required(str)
#     name = Required(str)
#     gender = Required(str)
#     address = Required(str)
#     phone_number = Required(str)
#     borrowedbook = Set('BorrowedBook')
#     returnedbook = Set('ReturnedBook')

# class BookCategory(db.Entity):
#     _table_ = "tbl_book_category"
#     id_book_category = PrimaryKey(int, auto=True)
#     category = Required(str, unique=True)
#     book = Set('Book')

# class BookAuthor(db.Entity):
#     _table_ = "tbl_book_author"
#     id_book_author = PrimaryKey(int, auto=True)
#     name = Required(str, unique=True)
#     email = Optional(str)
#     gender = Optional(str)
#     address = Optional(str)
#     phone_number = Optional(str)
#     book = Set('Book')

# class Publisher(db.Entity):
#     _table_ = "tbl_book_publisher"
#     id_book_publisher = PrimaryKey(int, auto=True)
#     name = Required(str, unique=True)
#     email = Optional(str)
#     address = Optional(str)
#     phone_number = Optional(str)
#     book = Set('Book')

# class Book(db.Entity):
#     _table_ = "tbl_book"
#     id_book = PrimaryKey(int, auto=True)
#     stock = Required(int)
#     book_title = Required(str)
#     book_category = Required(BookCategory,column='id_book_category')
#     book_author = Required(BookAuthor,column='id_book_author')
#     book_publisher = Required(Publisher,column='id_book_publisher')
#     borrowedbook = Set('BorrowedBook')

# class BorrowedBook(db.Entity):
#     _table_ = "tbl_borrowed_book"
#     id_book_borrowed = PrimaryKey(int, auto = True)
#     loan_date = Required(date)
#     date_of_return = Optional(date)
#     status = Required(bool)
#     user = Required(User,column='id_user')
#     admin = Optional(Admin,column='id_admin')
#     book = Required(Book, column='id_book')
#     returnedbook = Set('ReturnedBook')

# class ReturnedBook(db.Entity):
    # _table_ = "tbl_returned_book"
    # id_book_returned = PrimaryKey(int, auto = True)
    # date_of_returned = Required(date)
    # late_charge = Required(int)
    # book_borrowed = Required(BorrowedBook, column='id_book_borrowed')

 
db.bind(provider=os.getenv('DB_PROVIDER'),user=os.getenv('DB_USER'),password=os.getenv('DB_PASSWORD'),host=os.getenv("DB_HOST"),database=os.getenv("DB_NAME"))
db.generate_mapping(create_tables=False)
Pony(app)


# USER REGISTER
@app.route("/auth/register", methods=['POST'])
def register():
    try:
        jsonBody = request.json
        email = jsonBody['email']
        cekUsername = db.select(f"select *from public.user where username = '{jsonBody['username']}' or email = '{jsonBody['email']}' ")
        #nani = db.select(f"select username,password,email,name from public.user where email = '{email}' and username='{jsonBody['username']}'")
        
        if jsonBody['username'] == "" or jsonBody['password'] == "" or jsonBody['email'] == "" or jsonBody['name'] =="":
            response ={
                "data": "Bad Request",
                "message": "Ada data yang tidak benar"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif cekUsername:
            response ={
                "data": "Bad Request",
                "message": "Username / email sudah terdaftar"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif email_regex.match(email):
            hashpass = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
            query = f"insert into public.user(username,password,email,name,gender) values ('{jsonBody['username']}','{hashpass.hexdigest()}','{jsonBody['email']}','{jsonBody['name']}','{jsonBody['gender']}')"
            data = db.execute(query) 
            response  ={
                "data": jsonBody,
                "message": "Data inserted"
            }
            return jsonify(response), HTTPStatus.OK
        else:
            response={
                "data": "bad request",
                "message": "email is not valid"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY

# USER LOGIN
@app.route("/auth/login",methods=['POST'])
def login():
    try:
        jsonBody = request.json
        hashpass = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
        user = db.select(f"select *from public.user where username = '{jsonBody['username']}' and password = '{hashpass.hexdigest()}'")
        #session['username'] = hashpass
        if not user:
            response = {
                "data": "Bad Request",
                "message": "Username/ password salah"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        
        access_token = create_access_token(identity=user)
        response = {
            "data": access_token,
            "message": "Berhasil Login"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY

# USER LOGOUT
@app.route("/auth/logout",methods=['DELETE'])
def logout():
    if 'username' in session:
        session.pop('username',None)
        response = {
            "data": "400",
            "message": "Already approved"
        }
        return jsonify(response), HTTPStatus.OK



# USER LIST
@app.route("/list/user")
def listUser():
    listUser = db.execute(f"select pk_user,name,username,email,password,gender from public.user")
    y = []
    for i in listUser:
        y.append(i)
    listselectbuku = []
    for i in y:
        dictbuku ={
            "id": i[0],
            "name": i[1],
            "username": i[2], 
            "email": i[3],
            "password": i[4],
            "gender": i[5]
        }
        listselectbuku.append(dictbuku)
    
    response = {
            "data": listselectbuku,
            "message": "Success"
        }
    
    return jsonify(response),HTTPStatus.OK

# LIST USER UPDATE
@app.route("/update/user/<id>")
def listUpdateUser(id):
    try:
        querySelectById = db.execute(f"select pk_user,username,password,email,name,gender from public.user where pk_user = {id}")
        data = []
        for i in querySelectById:
            data.append({
                "username": i[1],
                "password": i[2],
                "email": i[3],
                "name": i[4],
                "gender": i[5]
            })
        if not data:
            respon = {
                "data": "no data",
                "message": "bad"
            }
            return jsonify(respon), HTTPStatus.BAD_REQUEST
        respon = {
            "data": data[0],
            "message": "data is found"
        }
        return jsonify(respon),HTTPStatus.OK
        
    except Exception as respError:
        respon = {
            "data": str(respError),
            "message": "bad gateway"
        }
        return jsonify(respon),HTTPStatus.BAD_GATEWAY

# USER UPDATE
@app.route("/update/user/<id>",methods=['PUT'])
def updateUser(id):
    bodyJson = request.json
    hashpass = hashlib.md5((bodyJson['password']+os.getenv("SALT_PASSWORD")).encode())
    queryUpdate = f"update public.user set username='{bodyJson['username']}' ,password = '{hashpass.hexdigest()}',email='{bodyJson['email']}',name='{bodyJson['name']}',gender='{bodyJson['gender']}' where pk_user = {id}"
    db.execute(queryUpdate)
    response = {
        "data": "Update",
        "message": "Data updated"
    }
    return jsonify(response), HTTPStatus.ACCEPTED

# USER DELETE
@app.route("/delete/user/<id>",methods=['DELETE'])
def deleteUser(id):
    try:
        selectById = (f"select pk_user from public.user where pk_user = {id}")
        data = []
        for i in db.execute(selectById):
            data.append({
                "id": i[0]
            })
        if not data:
            response = {
                "data": "no data",
                "message": "bad request"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        else:
            deleteById = (f"delete from public.user where pk_user = {id}")
            db.execute(deleteById) 
            response = {
            "data": "delete tasklist",
            "message": "Delete Success"
        } 
        return jsonify(response), HTTPStatus.ACCEPTED
    except Exception as respError:
        response={
            "data": str(respError),
            "message": "bad gateway"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY

# USER BOROWING BOOK
@app.route("/borrowBook/<id>",methods=['POST'])
@jwt_required()
def borrowBook(id):
    current_user = get_jwt_identity()
    id_user = current_user[0][0]
    try:
        a = db.execute(f"select stok from book where pk_buku = {id} ")
        for a in a:
            a = a
        b = sum(a) 
        borrow = db.select(f"select * from borrowing where fk_user = {id_user} and fk_book = {id}")
        if borrow:
            response = {
                    "data": "Bad Request",
                    "message": "You already borrow"
                }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        if b > 0:
            db.execute(f"insert into borrowing(loan_date,date_of_return,fk_user,fk_book) values(NOW(),NOW() + INTERVAL '7 days',{id_user},{id}) ")
            db.execute(f"update book set stok = (stok - 1) where pk_buku = {id}")
            respons = {
                "data": "ok",
                "message": "Loan success please wait for confirmation"
            }
            return jsonify(respons), HTTPStatus.OK
        elif b == 0:
            respons ={
                "data": "No book found",
                "message": "All book is booked"
            }
            return jsonify(respons), HTTPStatus.BAD_REQUEST
        
       
    except Exception as err:
        respons = {
            "data": str(err),
            "message": "Loan not success"
        }
        return jsonify(respons),HTTPStatus.BAD_GATEWAY

# ADMIN REGISTER
@app.route("/auth/registeradmin", methods=['POST'])
def registerAdm():
    try:
        jsonBody = request.json
        email = jsonBody['email']
        if jsonBody['username'] == "" or jsonBody['password'] == "" or jsonBody['email'] == "" or jsonBody['name'] =="":
            response ={
                "data": "Bad Request",
                "message": "Ada data yang tidak benar"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif email_regex.match(email):
            hashpass = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
            query = f"insert into public.admin(username,password,email,name,gender) values ('{jsonBody['username']}','{hashpass.hexdigest()}','{jsonBody['email']}','{jsonBody['name']}','{jsonBody['gender']}')"
            data = db.execute(query) 
            response  ={
                "data": jsonBody,
                "message": "Data inserted"
            }
            return jsonify(response), HTTPStatus.OK
        else:
            response={
                "data": "bad request",
                "message": "email is not valid"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
    except Exception as err:
        response ={
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY
    
# ADMIN LOGIN
@app.route("/auth/loginadmin",methods=['POST'])
def loginAdmin():
    try:
        jsonBody = request.json
        hashpass = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
        user = db.select(f"select *from public.admin where username = '{jsonBody['username']}' and password = '{hashpass.hexdigest()}'")
        if not user:
            response = {
                "data": "Bad Request",
                "message": "Username/ password salah"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        access_token = create_access_token(identity=user)
        response = {
            "data": f"Token : {access_token}",
            "message": "Berhasil Login"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY

# ADMIN ACC BOOK
@app.route("/approveBorrow/<id>",methods=['PUT'])
@jwt_required()
def approveBorrow(id):
    current_admin = get_jwt_identity()
    id_admin = current_admin[0][0]
    
    try:
        approve = f"update borrowing set fk_admin = {id_admin} where pk_borrowing = {id}"
        select = db.select(f"select pk_borrowing from borrowing where fk_admin is null")
        if select:
            response = {
                "data": "400",
                "message": "Already approved"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        db.execute(approve)
        response = {
                "data": "a",
                "message": "Approve accepted"
            }
        return jsonify(response),HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY
   
# CREATE BOOK
@app.route("/create/book")
def createBook():
    pass

# LIST BOOK
@app.route("/list/book")
#s@jwt_required()
def bookList():
    selectbuku = db.execute(f"select a.pk_buku,a.stok,a.judul_buku,b.types,c.author_name,d.publisher_name from book as a left join booktypes as b on (a.fk_book_types = b.pk_book_type) left join author as c on (a.fk_author = c.pk_author) left join publisher as d on (a.fk_publisher = d.pk_publisher)")
    
    y = []
    for i in selectbuku:
        y.append(i)
    listselectbuku = []
    for i in y:
        dictbuku ={ 
            "judul_buku": i[2],
            "stok": i[1], 
            "book_types": i[3],
            "author": i[4],
            "publisher": i[5]
        }
        listselectbuku.append(dictbuku)
    response = {
            "data": listselectbuku,
            "message": "Success"
        }
    return jsonify(response),HTTPStatus.OK

# DETAIL BOOK
@app.route("/detail/book/<id>")
def bookDetail(id):
    bookselectbyid = db.execute(f"select a.loan_date, a.date_of_return,b.name,c.name,d.judul_buku, extract(day from a.date_of_return) - extract(day from now()) from borrowing as a left join admin as b on(a.fk_admin = b.pk_admin) left join public.user as c on(a.fk_user = c.pk_user) left join book as d on(a.fk_book = d.pk_buku) where fk_book = {id}")
    
    y = []
    for i in bookselectbyid:
        y.append(i) 
    listselectbuku = []
    for i in y:
        dictbuku ={ 
            "_judul_buku": i[4],
            "loan_date": i[0],
            "date_of_return": i[1],
            "sisa hari peminjaman": i[5], 
            "nama peminjam": i[3],
            "nama yg meminjamkan": i[2]
        }
        listselectbuku.append(dictbuku)
    response = {
            "data": listselectbuku,
            "message": "Success"
        }
    return jsonify(response), HTTPStatus.OK

# DETAIL BOOK EXPIRED
# @app.route("/detail/bookexp/<id>")
# def bookexpDetail(id):
#     data = db.execute(f"select  from borrowing;")
    

# CREATE BOOK CATEGORY
@app.route("/create/category",methods=['POST'])
def createBookCategory():
    pass

# LIST BOOK CATEGORY
@app.route("/list/category")
def bookCategoryList():
    listBookCategory = db.execute(f"select * from booktypes")
    y = []
    for i in listBookCategory:
        y.append(i)
    listcategory = []
    for i in y:
        category ={ 
            "_id": i[0],
            "category": i[1]
        }
        listcategory.append(category)
    
    response = {
        "data": listcategory,
        "message": "List Category of Book"
    }
    return jsonify(response), HTTPStatus.OK

# CREATE BOOK AUTHOR
@app.route("/create/author",methods=['POST'])
def bookAuthor():
    pass

# LIST BOOK AUTHOR
@app.route("/list/author")
def bookAuthorList():
    listBookAuthor = db.execute(f"select author_name from author")
    for i in listBookAuthor:
        dictAuthor = {
            "author_name" : i[0]
        }

    response = {
        "data": dictAuthor,
        "message": "List Author of Book"
    }
    return jsonify(response), HTTPStatus.OK

# CREATE BOOK PUBLISHER
@app.route("/create/publisher",methods=['POST'])
def bookPublisher():
    pass

# LIST BOOK PUBLISHER
@app.route("/list/publisher")
def bookPublisherList():
    listBookPublisher = db.execute(f"select publisher_name from publisher")
    for i in listBookPublisher:
        dictPublisher = {
            "publisher_name": i[0]
        }
    response = {
        "data": dictPublisher,
        "message": "List Publisher of Book"
    }
    return jsonify(response), HTTPStatus.OK

