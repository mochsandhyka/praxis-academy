from flask import Flask, session,request,redirect,url_for
app = Flask(__name__)

app.secret_key = b'12f9631afeb4a6ce4d8cc641599e5b3db8ce7dc351afd4f1fa4829a4acd7725a'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]} '
    return 'you are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))