

# Created by Sachin Dev on 01/06/18

from flask import Flask

from common.database import Database
from models.users.views import user_blueprint

app = Flask(__name__)
app.config.from_object('config')
app.secret_key='sachin'


@app.before_first_request
def _init_db():
    Database.initialize()


app.register_blueprint(user_blueprint, url_prefix='/users')