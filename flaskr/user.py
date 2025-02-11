from flask import (
    abort,
    Blueprint,
    current_app,
    g,
    jsonify,
    make_response,
    request,
    Response,
)

# from flaskr.auth import auth
from flaskr.extensions import db
from flaskr.models import User

user_bp = Blueprint("user", __name__, url_prefix="/user/<string:user_id>")


@user_bp.route("", methods=["POST"])
# @auth
def add_user(user_id: str) -> Response:
    """
    Add user record to DB.
    """
    # Extract data from payload as JSON and suppress errors so we can control response
    # behaviour
    payload = request.get_json(force=True, silent=True)
    current_app.logger.debug(f"Request payload: {payload}")
    if payload is None:
        current_app.logger.error("Request did not contain expected JSON payload")
        abort(400)

    try:
        user_name = payload["name"]
    except KeyError:
        current_app.logger.error("name not found in request payload")
        abort(400)

    try:
        password = payload["password"]
    except KeyError:
        current_app.logger.error("password not found in request payload")
        abort(400)

    user = User(user_id, user_name, password)
    db.session.add(user)
    db.session.commit()

    current_app.logger.debug(f"Added user {user.serialize}")

    return make_response("Success", 201)


@user_bp.route("")
# @auth
def get_user(user_id: str) -> Response:
    """
    Fetch user record from DB.
    """
    user = db.get_or_404(User, (user_id))
    return make_response(jsonify(user.serialize()), 200)
