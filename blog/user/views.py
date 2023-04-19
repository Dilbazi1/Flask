from werkzeug.exceptions import NotFound
from flask import Blueprint
from flask import render_template, redirect
from flask_login import login_required

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
USERS = {
    1: "Ivan",
    2: "Jon",
    3:  "Mary"
}

@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
# @login_required
def profile(pk: int):
    from blog.models.user import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f'User {pk} doesnt exist')

    return render_template('users/profile.html',
                           user=_user
                           )


def get_user_name(pk: int):
        if pk in USERS:
            user_name = USERS[pk]
        else:
            raise NotFound(f'User id {pk} not found')
        return user_name
