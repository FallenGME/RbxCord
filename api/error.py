from flask import Flask, jsonify

app = Flask(__name__)

# Example routes
@app.route("/")
def home():
    return jsonify(message="Welcome to the homepage!")

@app.route("/dang")
def dang():
    return jsonify(message="DANG page!")

@app.errorhandler(Exception)
def handle_error(e):
    code = getattr(e, "code", 500)
    description = getattr(e, "description", str(e))

    response = {
        "status": code,
        "error": description
    }
    return jsonify(response), code