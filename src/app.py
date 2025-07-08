from flask import Flask, jsonify
from src.routes.encode import encode_blueprint
from src.routes.sign import sign_blueprint
from src.exceptions import BadRequestException, ForbiddenException
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.register_blueprint(encode_blueprint, url_prefix="/v0/crypto")
app.register_blueprint(sign_blueprint, url_prefix="/v0/crypto")


@app.errorhandler(BadRequestException)
@app.errorhandler(422)
@app.errorhandler(415)
@app.errorhandler(400)
def handle_bad_request(e):
    return (
        jsonify({"error": "bad_request", "message": str(e)}),
        400,
    )


@app.errorhandler(ForbiddenException)
@app.errorhandler(403)
def forbidden(e):
    return (
        jsonify({"error": "forbidden", "message": str(e)}),
        403,
    )


@app.errorhandler(500)
def internal_error(e):
    return (
        jsonify({"error": "internal_server_error", "message": str(e)}),
        e.code,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
