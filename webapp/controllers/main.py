from flask        import Blueprint, flash, redirect, render_template, url_for
from webapp.forms import LoginForm, RegisterForm

main_blueprint = Blueprint(
    "main",
    __name__,
    template_folder="../templates/main"
)

@main_blueprint.route("/")
def index():
    return redirect(url_for("sb.home"))

@main_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("You have been logged in.", category="success")
        return redirect(url_for('sb.home'))
    return render_template("login.html", form=form)

@main_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User()
        new_user.email = form.email.data
        new_user.password = form.password.data
        new_user.username = form.username.data
        db.session.add(new_user)
        db.session.commit()
        flash("your user has been created, please login.", category="success")
        return redirect(url_for(".login"))
    return render_template("register.html", form=form)