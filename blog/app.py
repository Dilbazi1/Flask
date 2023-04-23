import os
from flask import Flask,redirect,url_for
from blog.auth.views import auth
from blog.report.views import report
from blog.user.views  import user
from blog.article.views  import article
from blog.models.database import db
from flask_login import LoginManager

login_manager = LoginManager()
def create_app()->Flask:
    app=Flask(__name__)
    register_blueprints(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = '4s6=rc(wpw#+qxas@e$^_#p_jx!_#bsw=1&u*i-qp@u%+*q&&*f'

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from .models.user import  User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('auth.login'))





    cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app

def register_blueprints(app:Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.config["SECRET_KEY"] = "qwasaersdadafafafafaasdas"

