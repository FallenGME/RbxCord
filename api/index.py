from quart import Quart, request, Response
import requests

app = Quart(__name__)

DISCORD_BASE = "https://discord.com/api/webhooks/"

@app.route("/api/webhooks/<path:token>", methods=["POST", "PATCH", "DELETE"])
async def proxy(token):
    discord_url = f"{DISCORD_BASE}{token}"
    method = request.method
    headers = {"Content-Type": request.headers.get("Content-Type", "application/json")}
    data = await request.get_data()

    response = requests.request(method, discord_url, data=data, headers=headers)

    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get("Content-Type", "application/json")
    )

@app.route("/api/<path:anything>")
async def fallback(anything):
    return {"error": "Unavailable"}, 404

handler = app
