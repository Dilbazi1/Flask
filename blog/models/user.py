from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)

    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
