from dotenv import load_dotenv

load_dotenv()

from flask import Flask, jsonify
from src.routes.encode import encode_blueprint
from src.routes.sign import sign_blueprint
from src.exceptions import BadRequestException, ForbiddenException


app = Flask(__name__)

app.register_blueprint(encode_blueprint, url_prefix="/v0/crypto")
app.register_blueprint(sign_blueprint, url_prefix="/v0/crypto")


@app.errorhandler(400)
@app.errorhandler(415)
@app.errorhandler(422)
@app.errorhandler(BadRequestException)
def handle_bad_request(e):
    message = getattr(e, "description", str(e))
    return jsonify({"error": "bad_request", "message": message}), 400


@app.errorhandler(403)
@app.errorhandler(ForbiddenException)
def handle_forbidden(e):
    message = getattr(e, "description", str(e))
    return jsonify({"error": "forbidden", "message": message}), 403


@app.errorhandler(500)
def internal_error(e):
    return (
        jsonify({"error": "internal_server_error", "message": str(e)}),
        e.code,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
