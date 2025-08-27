from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify(message="hi ther")

@app.route("/home")
def home_redirect():
    return redirect(url_for("root"))
