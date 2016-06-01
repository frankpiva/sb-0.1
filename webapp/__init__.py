from controllers.sb    import sb_blueprint
from controllers.main  import main_blueprint
from flask             import Flask
from webapp.models     import db
from webapp.extensions import bcrypt

def create_app(object_name):
    """
    A flask application factory as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    :param   object_name: the python path of the config object
                        e.g. project.config.ProdConfig
    :return: app: The StudyBuddy application.
    """
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(sb_blueprint)

    return app

if __name__ == "__main__":
    app = app =create_app("project.config.ProdConfig")
    app.run()