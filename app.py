import logging
import json

import flask


app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("home.html")


@app.route("/contact-us")
def home():
    return flask.render_template("contact-us.html")

