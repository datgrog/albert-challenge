from flask import Flask, jsonify
from src.routes import encode_blueprint

app = Flask(__name__)

app.register_blueprint(encode_blueprint, url_prefix="/v0/crypto")


@app.errorhandler(415)
@app.errorhandler(400)
def handle_bad_request(e):
    return (
        jsonify({"error": "bad_request", "message": e.description, "code": e.code}),
        e.code,
    )


@app.errorhandler(500)
def internal_error(e):
    return (
        jsonify(
            {"error": "internal_server_error", "message": e.description, "code": e.code}
        ),
        e.code,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
