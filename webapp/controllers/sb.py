import datetime
from flask        import render_template, Blueprint
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
@sb_blueprint.route("/<int:page>")
def home(page=1):
    return render_template(
        "home.html",
    )