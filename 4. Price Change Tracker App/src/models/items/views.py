

# Created by Sachin Dev on 01/06/18

from flask import Blueprint


item_blueprint = Blueprint("items",__name__)

@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass


@item_blueprint.route('/load')
def load_item():
    """
    Loads an item's data using store and return JSON representation of it.

    """
    pass