from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from blog.models.database import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)

    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    author = relationship("Author", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey("authors.id"), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
