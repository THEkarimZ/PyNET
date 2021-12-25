import os
from flask import *
import pygame as pg
import sys
app = Flask(__name__)
app.secret_key = os.urandom(128)
players = {
    "@Roma": 0,
    "@Rayan": 0,
    "@Timur": 0,
    "@Karim": 0
}



@app.route("/admpass.html")
def redir_admin():
    psw = request.args.get("psw")
    if psw == "ADMIN":
        session["adm"] = "True"
        return redirect("/admin-panel/")
    else:
        return render_template("nosuch.html")

# Вход в аккаунт админа
@app.route("/admin-password/")
def admin_check():
    return f"""<form action="/admpass.html">
    <p>Введите пароль админа</p>
    <p>
    <input type="password" name="psw" placeholder="Введите пароль">
    <input type="submit">
    </p>
</form>"""


# Корень сайта
@app.route("/")
def index():
    if "adm" in session and session["adm"] == "True":
        return render_template("admin-ui.html")
    if "username" not in session or session["username"] not in players:
        return render_template("login.html")
    return render_template("game.html", username=session["username"])


@app.route("/login/")
def login():
    uname = request.args.get("username")
    if uname == "@Admin":
        return redirect("/admin-password/")
    if uname in players:
        session["username"] = uname
        session.modified = True
        return redirect("/main-page/")
    else:
        return render_template("nosuch.html")
@app.route("/off.html/")
def off():
    sys.exit()
@app.route("/admin-panel/")
def panel():
    return render_template("nocode.html")



app.run(host="0.0.0.0", port=8000)
