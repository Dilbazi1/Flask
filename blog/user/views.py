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
@user.route('/<pk>')
def get_user(pk:int):
    return pk
