from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.database import Base, engine
from app.domain.entities import Notification
from sqlalchemy.orm import Session
from app.infrastructure.repositories import NotificationRepository

client = TestClient(app)

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    with Session(engine) as session:
        session.query(Notification).delete()
        session.commit()

def test_create_notification():
    response = client.post("/notifications", json={
        "user_id": 1,
        "message": "Test notification",
        "read_status": False
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Test notification"

def test_get_notifications():
    client.post("/notifications", json={
        "user_id": 1,
        "message": "Test notification",
        "read_status": False
    })
    response = client.get("/notifications/1")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_mark_as_read():
    response = client.post("/notifications", json={
        "user_id": 1,
        "message": "Test notification",
        "read_status": False
    })
    notification_id = response.json()["id"]
    response = client.put(f"/notifications/{notification_id}/read")
    assert response.status_code == 200
    assert response.json()["read_status"] is True

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}