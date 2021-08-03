from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///project.db'

    db.init_app(app)
    migrate.init_app(app, db)

    from .main_views import main_bp
    app.register_blueprint(main_bp)

    return app


if __name__  == "__main__":
    app = create_app()
    app.run(debug=True)