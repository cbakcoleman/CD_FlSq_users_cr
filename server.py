from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("create.html")

@app.route("/read_all")
def all_users():
    all_users = User.get_all()
    print(all_users)
    return render_template("read_all.html", all_users = all_users)

@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    }
    new_user = User.create_user(data)
    return redirect('/read_all')
            
if __name__ == "__main__":
    app.run(debug=True)