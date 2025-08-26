import os
from flask import Flask, jsonify

app = Flask(__name__)
os.environ.get("REPLICATE_API_TOKEN")

@app.route("/")
def index():
    return jsonify({
        "message": "RbxCord is running. This is a private website.",
        "status": "ok",
        "Github": "https://github.com/FallenGME/RbxCord/issues"
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "message": "RbxCord is running. This is a private website.",
        "status": "ok",
        "Github": "https://github.com/FallenGME/RbxCord/issues"
    }), 404
