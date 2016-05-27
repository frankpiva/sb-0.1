import os

from flask.ext.script          import Manager, Server
from flask.ext.script.commands import ShowUrls
from flask.ext.migrate         import Migrate, MigrateCommand
from webapp                    import create_app
from webapp.models             import db, User

# default to dev config
env = os.environ.get("WEBAPP_ENV", "DEV")
app = create_app("webapp.config.%sConfig" % env.capitalize())

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User
    )

if __name__ == "__main__":
    manager.run()