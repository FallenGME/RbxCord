from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    response = {
        "status": "success",
        "message": "Welcome! This API was crafted with care by FallenGME.",
        "author": "FallenGME",
        "repository": "https://github.com/FallenGME/RbxCord",
        "api_version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "docs": "/docs"
    }
    return jsonify(response)

app.errorhandler(404)
def not_found(e):
    return jsonify({
        "status": "error",
        "repository": "https://github.com/FallenGME/RbxCord",
        "message": "The requested resource was not found."
    }), 404