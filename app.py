from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/course/")
def course():
    return render_template("cource.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/accounts/login/")
def login():
    return render_template("login.html")

@app.route("/accounts/signup/")
def signup():
    return render_template("signup.html")

@app.route("/accounts/password/reset/")
def reset():
    return render_template("reset.html")

@app.errorhandler(404)
def notfound(e):
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port= 5000)
