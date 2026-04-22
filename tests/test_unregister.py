def test_unregister_success(client):
    # Arrange: use a pre-populated participant from Chess Club
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_unregister_activity_not_found(client):
    # Arrange
    activity = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_not_signed_up(client):
    # Arrange
    activity = "Art Studio"
    email = "ghost@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"
