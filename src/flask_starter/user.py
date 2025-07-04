from flask import (
    abort,
    Blueprint,
    current_app,
    jsonify,
    make_response,
    request,
    Response,
)

# from flask_starter.auth import auth
from flask_starter.extensions import db
from flask_starter.models import User

user_bp = Blueprint("user", __name__, url_prefix="/user/<string:user_id>")


@user_bp.route("", methods=["POST"])
# @auth
def add_user(user_id: str) -> Response:
    """
    Add user record to DB.
    """
    user = User(user_id, "", "")
    db.session.add(user)
    db.session.commit()

    current_app.logger.debug(f"Added user {user.serialize}")

    return make_response("Success", 201)


@user_bp.route("", methods=["PUT"])
# @auth
def update_user(user_id: str) -> Response:
    """
    Update user record in DB.
    """
    # Extract data from payload as JSON and suppress errors so we can control response
    # behaviour
    payload = request.get_json(force=True, silent=True)
    current_app.logger.debug(f"Request payload: {payload}")
    if payload is None:
        current_app.logger.error("Request did not contain expected JSON payload")
        abort(400)

    args = {}  # mapping of db field name to new value
    try:
        args["name"] = payload["name"]
    except KeyError:
        pass

    try:
        args["password"] = payload["password"]
    except KeyError:
        pass

    if not args:
        current_app.logger.error(
            "Request did not contain expected keys in JSON payload"
        )
        abort(400)

    user = db.get_or_404(User, (user_id))

    if "name" in args:
        user.name = args["name"]
    if "password" in args:
        user.password = args["password"]

    db.session.commit()

    current_app.logger.debug(f"Updated user {user.serialize}")

    return make_response("Success", 201)


@user_bp.route("")
# @auth
def get_user(user_id: str) -> Response:
    """
    Fetch user record from DB.
    """
    user = db.get_or_404(User, (user_id))
    return make_response(jsonify(user.serialize()), 200)
