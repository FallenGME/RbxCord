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
