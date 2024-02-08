from flask import Flask,render_template,request,redirect
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    return redirect("/users")


@app.route('/users')
def users():
    return render_template("Users.html",users=User.get_all())

@app.route("/users/new")
def new_users():
    return render_template("index.html")

@app.route("/users/create",methods=["POST"])
def create():
    User.create(request.form)
    return redirect('/users')



if (__name__)=="__main__":
    app.run(debug=True, port=5001)