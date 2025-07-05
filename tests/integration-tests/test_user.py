import json


def test_create_user(client):
    # Create a user
    resp = client.post(
        "/user",
        data=json.dumps({"id": "tesftusefr", "name": "Test User"}),
        content_type="application/json",
    )
    assert resp.status_code == 201


def test_get_user(client):
    # Create a user first
    client.post(
        "/user",
        data=json.dumps({"id": "getuser", "name": "Get User"}),
        content_type="application/json",
    )

    # Retrieve the user
    resp = client.get("/user/getuser")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["id"] == "getuser"
    assert data["name"] == "Get User"


def test_update_user(client):
    # Create a user
    client.post(
        "/user",
        data=json.dumps({"id": "updateuser", "name": "Old Name"}),
        content_type="application/json",
    )

    # Update the user name
    resp = client.put(
        "/user/updateuser",
        data=json.dumps({"name": "New Name"}),
        content_type="application/json",
    )
    assert resp.status_code == 200

    # Verify the update
    resp = client.get("/user/updateuser")
    data = resp.get_json()
    assert data["name"] == "New Name"


def test_delete_user(client):
    # Create a user
    client.post(
        "/user",
        data=json.dumps(
            {
                "id": "deleteuser",
                "name": "ToDelete",
            }
        ),
        content_type="application/json",
    )

    # Delete the user
    resp = client.delete("/user/deleteuser")
    assert resp.status_code == 204

    # Verify deletion
    resp = client.get("/user/deleteuser")
    assert resp.status_code == 404


def test_get_nonexistent_user(client):
    resp = client.get("/user/doesnotexist")
    assert resp.status_code == 404


def test_create_user_missing_id(client):
    resp = client.post(
        "/user",
        data=json.dumps({"name": "No ID"}),
        content_type="application/json",
    )
    assert resp.status_code == 400


def test_update_user_no_fields(client):
    # Create a user
    client.post(
        "/user",
        data=json.dumps({"id": "nofields", "name": "Name"}),
        content_type="application/json",
    )

    # Attempt to update with empty payload
    resp = client.put(
        "/user/nofields",
        data=json.dumps({}),
        content_type="application/json",
    )
    assert resp.status_code == 400
