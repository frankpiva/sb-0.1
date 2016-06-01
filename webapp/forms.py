from flask_wtf          import Form, RecaptchaField
from webapp.models      import User
from wtforms            import BooleanField, PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(Form):
    password = PasswordField("Password", [DataRequired()])
    remember = BooleanField("Remember Me")
    username = StringField("Username", [
        DataRequired(),
        Length(max=255)
    ])

    def validate(self):
        # Check to see if data passes validators.
        check_validate = super(LoginForm, self).validate()
        if not check_validate:
            return False

        # Check to see if the user exists.
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append("Invalid username or password!")
            return False

        # Check to see if the passwords match.
        if not user.check_password(self.password.data):
            self.username.errors.append("Invalid username or password!")
            return False

        return True

class RegisterForm(Form):
    confirm = PasswordField("Confirm Password", [
        DataRequired(),
        EqualTo("password")
    ])
    email = StringField("Email Address", [
        DataRequired(),
        Length(max=255)
    ])
    password = PasswordField("Password", [
        DataRequired(),
        Length(min=8)
    ])
    recaptcha = RecaptchaField()
    username = StringField("Username", [
        DataRequired(),
        Length(max=255)
    ])

    #recaptcha = RecaptchaField()

    def validate(self):
        # Check to see if data passes validators.
        check_validate = super(RegisterForm, self).validate()
        if not check_validate:
                return False

        # Check to see if email address is already in use.
        email_exists = User.query.filter_by(email=self.email.data).first()
        if email_exists:
            self.email.errors.append("That email address already has an account associated with it!")
            return False

        # Check to see if username is already in use.
        username_exists = User.query.filter_by(username=self.username.data).first()
        if username_exists:
            self.username.errors.append("User with that name already exists!")
            return False

        return True