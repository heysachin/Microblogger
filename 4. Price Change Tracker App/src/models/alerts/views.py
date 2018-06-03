

# Created by Sachin Dev on 01/06/18

from flask import Blueprint


alert_blueprint = Blueprint('alerts',__name__)


@alert_blueprint.route('/new' , methods=['POST'])
def create_alert():
    pass


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate(alert_id):
    pass


@alert_blueprint.route('/alert/<string:alert_id>')
def get_alert_page(alert_id):
    pass


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
    pass