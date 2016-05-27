class Config(object):
    SECRET_KEY = "@dd3r@11"

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"