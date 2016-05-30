from flask.ext.sqlalchemy import SQLAlchemy

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
               " id:       {}\n" \
               " email:    {}\n" \
               " password: {}\n" \
               " username: {}>" \
               "".format(self.id, self.email, self.password, self.username)

    # TODO: FIX THIS METHOD TO USE BCRYPT DON'T FORGET TO SETUP AND IMPORT
    def check_password(self, password):
        return True

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)