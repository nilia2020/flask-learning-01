from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
clubes = [
    "River",
    "Boca",
    "Independiente",
    "Racing",
    "San Lorenzo",
    "Huracan",
    "Estudiantes",
    "Velez",
]


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/show_adress"))
    response.set_cookie("user_ip", user_ip)
    return response


@app.route("/show_adress")
def show_adress():
    user_ip = request.cookies.get("user_ip")
    context = {"user_ip": user_ip, "clubes": clubes}
    return render_template("ip_info.html", **context)


app.run(host="0.0.0.0", port=3000, debug=True)
