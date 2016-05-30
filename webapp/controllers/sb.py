import datetime
from flask        import Blueprint, render_template
from sqlalchemy   import func
from webapp       import models
from webapp.forms import RegisterForm

sb_blueprint = Blueprint(
    "sb",
    __name__,
    template_folder="../templates/sb",
    url_prefix="/sb"
)

@sb_blueprint.route("/")
@sb_blueprint.route("/home")
def home():
    return render_template("home.html")

@sb_blueprint.route("/login")
def login():
    return render_template("login.html")

@sb_blueprint.route("/register")
def register():
    return render_template("register.html")