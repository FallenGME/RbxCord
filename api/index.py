import os

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "message": "RbxCord is running. Enjoy!",
        "creator": "FallenGME",
    }