from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/docs")
def docs():
    return jsonify(
        name="My API",
        version="1.0.0",
        description="A simple API running on Vercel with Flask",
        routes={
            "/": "API documentation",
            "/dang": "Returns a DANG message",
            "/home": "Redirects to /",
            "/something": "Example endpoint (replace with your own)"
        }
    )
