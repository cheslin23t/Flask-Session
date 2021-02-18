from flask import url_for, Flask, flash, render_template, request, make_response, flash, redirect
import werkzeug


users = {}
userids = {}
usernames = {}
app = Flask(__name__)
app.config['SECRET'] = '6LfylFYaAAAAANOM0EdY1ohBa-jVwojcuD6Mt_3I'
import os

def returnerr(msg, code):
    return render_template("error.html", msg=msg, code=code)

app.config['SECRET_KEY'] = 'uhh'
static = os.path.join('static')
@app.route('/', methods = ['GET'])
def home():
    userid = request.cookies.get('userid')
    

    
    
    if userid in usernames:


        username = usernames[userid]
        return render_template('home.html', username=username)
    return render_template('home.html')
@app.route("/admin")
def admin():
    userid = request.cookies.get('userid')
    

    
    
    if userid in usernames and not 0 or "0":

        if not userid in usernames:
            return returnerr("Please don't try to hack into the admin page - It won't work anyways ;)", "403 - Forbidden")
        username = usernames[userid] or None
        if username == None:
            return returnerr("Uhh, mind if you could tell me how you got here??", "403 - Forbidden")
        return render_template('admin.html', username=username)
    else:
        return returnerr("Sorry, please signin to access this page", "403 - Forbidden"), 403
@app.route('/login', methods = ['GET','POST'])
def login():
    username = request.cookies.get('username')
    if username:
        return render_template('login.html', username=username)
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            flash("Successful login", "success")
            resp = make_response(redirect('/'))
            resp.set_cookie('userid', userids[username])
            print(userids[username])
            return resp
        else:
            flash("Wrong username or password", "danger")
    return render_template('login.html')

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    users[username] = password
    usrid = hash(password)
    secret = app.config['SECRET']
    userids[username] = str(max(usrid, -usrid))
    usernames[str(max(usrid, -usrid))] = username
    return redirect("/login")

@app.route("/signup")
def signupindex():
    smile = os.path.join(static, 'smile.png')
    music = os.path.join(static, 'music.mp3')
    return render_template("signup.html", smile = smile, music = music)



@app.route('/logout', methods = ['GET'])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('userid')
    return resp

@app.errorhandler(404)
def page_not_found(e):
    return returnerr("Uhh, this page does not exist..", "404 - Not found"), 404
app.run('0.0.0.0',debug=True)