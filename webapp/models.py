from flask.ext.sqlalchemy import SQLAlchemy
from webapp.extensions    import bcrypt

db = SQLAlchemy()

class User(db.Model):
    id       = db.Column(db.Integer(), primary_key=True)
    email    = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(255), index=True)
    username = db.Column(db.String(255), index=True, unique=True)

    def __init__(self, email, password, username):
        self.email    = email
        self.password = password
        self.username = username

    def __repr__(self):
        return "USER RECORD\n" \
               "  id:       {}\n" \
               "  email:    {}\n" \
               "  password: {}\n" \
               "  username: {}\n" \
               "".format(self.id, self.email, self.password, self.username)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)