from flask import url_for, Flask, flash, render_template, request, make_response, flash, redirect
import werkzeug


users = {}
userids = {}
usernames = {}
app = Flask(__name__)
app.config['SECRET'] = '6LfylFYaAAAAANOM0EdY1ohBa-jVwojcuD6Mt_3I'
import os

app.config['SECRET_KEY'] = 'uhh'
static = os.path.join('static')
@app.route('/', methods = ['GET'])
def home():
    userid = request.cookies.get('userid')
    

    
    
    if userid in usernames:


        username = usernames[userid]
        return render_template('home.html', username=username)
    return render_template('home.html')

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

@app.route("/test")
def test():
    return render_template("test.html")
@app.route("/test", methods=['POST'])
def posttest():

    
    img = request.files['hi']
    os.path.join(img, werkzeug.secure_filename(img.filename))
    return render_template("test2.html", img=img)

@app.route('/logout', methods = ['GET'])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('userid')
    return resp

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>????????????????????</h1><br>" + str(e)
app.run('192.168.86.192',debug=True, port=80)