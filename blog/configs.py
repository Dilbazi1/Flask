import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = '4s6=rc(wpw#+qas@e$^_#p_jx!_#bsw=1&u*i-qp@u%+*q&&*f'
    SQLALCHEMY_DATABASE_URI = "sqlite:///../db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevConfig(BaseConfig):
    SECRET_KEY = '4s6=rc(wpw#+qas@e$^_#p_jx!_#bsw=1&u*i-qp@u%+*q&&*f'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True