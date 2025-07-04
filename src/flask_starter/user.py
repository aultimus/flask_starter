from flask import Blueprint, request, jsonify, current_app, abort, make_response
from flask_starter.extensions import db
from flask_starter.models import User  # adjust import if needed

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("", methods=["POST"])
def add_user():
    """
    Create a new user.
    """
    payload = request.get_json(force=True, silent=True)
    if not payload or "id" not in payload:
        abort(400, description="Missing user ID")

    user = User(
        id=payload["id"],
        name=payload.get("name", ""),
    )
    db.session.add(user)
    db.session.commit()

    current_app.logger.debug(f"Added user {user.serialize()}")
    return make_response("Created", 201)


@user_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    """
    Retrieve user by ID.
    """
    user = db.get_or_404(User, user_id)
    return jsonify(user.serialize())


@user_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update user by ID.
    """
    payload = request.get_json(force=True, silent=True)
    if not payload:
        abort(400, description="Missing JSON payload")

    user = db.get_or_404(User, user_id)

    updated = False
    if "name" in payload:
        user.name = payload["name"]
        updated = True

    if not updated:
        abort(400, description="No fields to update")

    db.session.commit()
    current_app.logger.debug(f"Updated user {user.serialize()}")
    return make_response("Updated", 200)


@user_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete user by ID.
    """
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return make_response("Deleted", 204)
