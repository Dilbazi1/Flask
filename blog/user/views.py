from werkzeug.exceptions import  NotFound
from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
USERS={
    1:'Alice',
    2:'Jon',
    3:'Mike'}


@user.route('/')
def user_list():
    return render_template('users/list.html',users=USERS)
@user.route('/<int:pk>')
def get_user(pk:int):
    try:
        user_name=USERS[pk]
    except KeyError:
      raise NotFound(f'User id {pk} not found')
    return render_template('users/details.html',user_name=user_name)
