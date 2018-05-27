# Created by Sachin Dev on 27/05/18

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_method():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
