from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from blog.models.database import db


class Author(db.model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')
