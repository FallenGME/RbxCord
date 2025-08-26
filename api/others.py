from quart import Quart, Response

app = Quart(__name__)

@app.route("/api/<path:all>", methods=["GET", "POST", "PATCH", "DELETE", "PUT"])
async def catch_all(all):
    return Response(
        "Unavailable",
        status=403,
        content_type="text/plain"
    )

handler = app