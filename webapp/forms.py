from flask_wtf          import Form
from wtforms            import StringField
from wtforms.validators import DataRequired, Length

class RegisterForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )