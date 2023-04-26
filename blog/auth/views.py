from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash
from blog.forms.user import UserRegisterForm

auth = Blueprint("auth", __name__, url_prefix="/auth", static_folder="../static")


@auth.route('register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))
    form = UserRegisterForm(request.form)
    return render_template(
        'auth/register.html',
        form=form,
    )


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template(
            "auth/login.html"
        )
    from ..models import User

    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Check your login details")
        return redirect(url_for(".login"))
    login_user(user)

    return redirect(url_for("user.profile", pk=user.id))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
