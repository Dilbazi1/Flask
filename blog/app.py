import os
from flask import Flask, redirect, url_for
from blog.auth.views import auth
from blog.report.views import report
from blog.user.views import user
from blog.article.views import article
from blog.author.views import author
from blog.models.database import db
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_admin import Admin
from blog.admin.__init__  import admin
from blog.api import init_api
login_manager = LoginManager()
# admin=Admin(name='Blog Admin Panel',template_mode='bootstrap4')


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_blueprints(app)

    app.config['SECRET_KEY'] = '4s6=rc(wpw#+qxas@e$^_#p_jx!_#bsw=1&u*i-qp@u%+*q&&*f'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)

    migrate = Migrate(app, db, compare_type=True)
    csrf = CSRFProtect()
    csrf.init_app(app)
    init_api(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    admin.init_app(app)
    from .models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('auth.login'))

    # cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
    # app.config.from_object(f"blog.config.{cfg_name}")

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.secret_key = 'secret key'
    return app


def register_blueprints(app: Flask):
    from blog import admin

    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(author)
    app.config["SECRET_KEY"] = "qwasaersdadafafafafaasdas"

