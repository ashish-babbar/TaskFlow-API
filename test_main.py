from fastapi.testclient import TestClient
from database import Base, engine
from main import app

client = TestClient(app)


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_signup_and_login():
    resp = client.post("/signup", json={"email": "a@test.com", "password": "pass123"})
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_create_and_list_task():
    signup = client.post("/signup", json={"email": "b@test.com", "password": "pass123"})
    token = signup.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    create = client.post("/tasks", json={"title": "Write resume bullets"}, headers=headers)
    assert create.status_code == 201
    assert create.json()["is_done"] is False

    listed = client.get("/tasks", headers=headers)
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_tasks_are_isolated_between_users():
    """User A should never see User B's tasks -- this is the ownership check
    that's easy to forget and a common interview question."""
    user_a = client.post("/signup", json={"email": "c@test.com", "password": "pass123"})
    token_a = user_a.json()["access_token"]
    client.post(
        "/tasks", json={"title": "A's private task"},
        headers={"Authorization": f"Bearer {token_a}"},
    )

    user_b = client.post("/signup", json={"email": "d@test.com", "password": "pass123"})
    token_b = user_b.json()["access_token"]
    listed_b = client.get("/tasks", headers={"Authorization": f"Bearer {token_b}"})

    assert listed_b.json() == []


def test_unauthenticated_request_is_rejected():
    resp = client.get("/tasks")
    assert resp.status_code == 401
