import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app() -> None:
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    f = config.factory(config_name if config_name else 'development') # ..ni idea que hace......
    app.config.from_object(f)
    f.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)

    # registramos los recoruces, ahora le agregamos ........
    #from app.resources import home, cabanas
    @app.shell_context_processor
    def ctx():
        return{
            "app": app,
            "db":db
        }
    return app