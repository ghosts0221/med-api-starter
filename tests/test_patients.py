import os
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db import database as db_module
from app.db.database import Base

TEST_DB = "test_app.db"


@pytest.fixture(autouse=True)
def _use_test_db(monkeypatch):
    # Point DB to a test sqlite file
    monkeypatch.setattr(db_module, "DATABASE_URL", f"sqlite:///{TEST_DB}")
    monkeypatch.setattr(
        db_module,
        "engine",
        db_module.create_engine(db_module.DATABASE_URL, connect_args={"check_same_thread": False}),
    )
    monkeypatch.setattr(
        db_module,
        "SessionLocal",
        db_module.sessionmaker(autocommit=False, autoflush=False, bind=db_module.engine),
    )

    # Recreate tables in test DB
    Base.metadata.drop_all(bind=db_module.engine)
    Base.metadata.create_all(bind=db_module.engine)

    yield

    # Cleanup
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


client = TestClient(app)


def test_create_and_list_patient():
    payload = {"patient_code": "P-001", "age": 28, "sex": "M"}
    r = client.post("/patients", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["patient_code"] == "P-001"
    assert data["age"] == 28

    r2 = client.get("/patients?limit=10&offset=0")
    assert r2.status_code == 200
    items = r2.json()
    assert len(items) == 1
    assert items[0]["patient_code"] == "P-001"


def test_duplicate_patient_code_returns_409():
    payload = {"patient_code": "P-dup", "age": 30, "sex": "F"}
    r1 = client.post("/patients", json=payload)
    assert r1.status_code == 201

    r2 = client.post("/patients", json=payload)
    assert r2.status_code == 409
