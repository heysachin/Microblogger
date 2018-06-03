

# Created by Sachin Dev on 01/06/18

from flask import Blueprint, request, render_template, session, url_for
from werkzeug.utils import redirect
from common.utils import Utils
from models.users.user import User
import models.users.errors as UserErrors

user_blueprint = Blueprint('users',__name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.html")


@user_blueprint.route('/check/<string:passd>')
def passed_value(passd):
    return " {} ".format(Utils.hash_password(passd))


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/register.html")


@user_blueprint.route('/alerts')
def user_alerts():
    return "This is alerts page!!"


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass