from flask import Flask, request
import CurrentDay
import json
import config

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>NEWS TICKER</h1>"
