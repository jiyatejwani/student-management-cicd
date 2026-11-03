import pytest
from app import create_app
from app.models import repository


@pytest.fixture
def client():
    """Fresh app with an empty store before each test, so tests stay independent."""
    repository._students.clear()
    repository._next_id = 1
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def sample_student():
    return {
        "name": "Asha Rao",
        "roll_number": "22CS001",
        "branch": "CSE",
        "email": "asha@example.com",
    }


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_list_students_empty(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_student(client):
    response = client.post("/students", json=sample_student())
    assert response.status_code == 201
    body = response.get_json()
    assert body["id"] == 1
    assert body["name"] == "Asha Rao"


def test_create_student_missing_field(client):
    bad = {"name": "No Email", "roll_number": "22CS002", "branch": "CSE"}
    response = client.post("/students", json=bad)
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_get_student(client):
    client.post("/students", json=sample_student())
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.get_json()["roll_number"] == "22CS001"


def test_get_student_not_found(client):
    response = client.get("/students/999")
    assert response.status_code == 404


def test_update_student(client):
    client.post("/students", json=sample_student())
    updated = sample_student()
    updated["branch"] = "ECE"
    response = client.put("/students/1", json=updated)
    assert response.status_code == 200
    assert response.get_json()["branch"] == "ECE"


def test_delete_student(client):
    client.post("/students", json=sample_student())
    response = client.delete("/students/1")
    assert response.status_code == 200
    follow_up = client.get("/students/1")
    assert follow_up.status_code == 404
