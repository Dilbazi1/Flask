from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models.database import db
from blog.models.user import User
from blog.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }