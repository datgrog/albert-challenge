from flask import Flask, Response, jsonify

app = Flask(__name__, static_url_path="/v0")


@app.route("/ping")
def ping() -> Response:
    return jsonify({"message": "pong"})
