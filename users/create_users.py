import flask
from flask import Flask
import os

app = Flask(__name__)


@app.route('/users/<id>', methods=['POST'])
def create(id):
    if os.path.exists("users/" + id + ".txt"):
        return flask.Response(status=500)
    else:
        f = open(id + ".txt", "w")
        return flask.Response(status=200)

