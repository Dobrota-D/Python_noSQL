import flask
from flask import Flask
import os

app = Flask(__name__)


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    if os.path.exists("users/" + id + ".txt"):
        os.remove("users/" + id + ".txt")
        return flask.Response(status=200)
    else:
        return flask.Response(status=500)
