

# Created by Sachin Dev on 01/06/18

from flask import Blueprint


store_blueprint = Blueprint('stores',__name__)


@store_blueprint.route('/store/<string:name>')
def store_page():
    pass