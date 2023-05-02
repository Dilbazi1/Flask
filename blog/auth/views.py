from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from blog.forms.user import UserRegisterForm, LoginForm
from blog.models.user import User
from blog.models.database import db

auth = Blueprint("auth", __name__, url_prefix="/auth", static_folder="../static")


@auth.route('register', methods=["GET", "POST"],endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))
    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('auth/register.html', form=form)

        _user = User(
            email=form.email.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            username=form.username.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)

    return render_template(
        'auth/register.html',
        form=form,
        error=errors,
    )


@auth.route("/login", methods=["GET", "POST"],endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))


    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()

        if not user:
            return render_template(
                "auth/login.html", form=form, error="username doesn't exist"
            )

        if not check_password_hash(user.password, form.password.data):
            return render_template(
                "auth/login.html", form=form, error="invalid username or password"
            )

        login_user(user)
        return redirect(url_for('user.profile', pk=user.id))
    return render_template("auth/login.html", form=form)



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
