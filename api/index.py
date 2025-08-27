from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

app.errorhandler(404)
def not_found(e):
    return jsonify({
        "status": "error",
        "repository": "https://github.com/FallenGME/RbxCord",
        "message": "The requested resource was not found."
    }), 404