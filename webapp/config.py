class Config(object):
    SECRET_KEY = "@dd3r@11"
    RECAPTCHA_PUBLIC_KEY = "6LfvdCETAAAAAA1H1g01fGq32GmsSj93WX0ZFHOP"
    RECAPTCHA_PRIVATE_KEY = "6LfvdCETAAAAAHUeAyvxw0uSEJnFTCiTJTNMTyyY"

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"