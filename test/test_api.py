import pytest
from fastapi.testclient import TestClient

from app.main import app

VALID_CAR = {
    "brand": "Ford",
    "model": "Utility Police Interceptor Base",
    "model_year": 2013,
    "mileage": 51000,
    "fuel_type": "E85 Flex Fuel",
    "engine": "300.0HP 3.7L V6 Cylinder Engine Flex Fuel Capability",
    "transmission": "6-Speed A/T",
    "accident": "At least 1 accident or damage reported",
    "engine_size": 3.7,
    "horsepower": 300,
}


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["model_loaded"] is True


def test_predict_valid(client):
    r = client.post("/predict", json=VALID_CAR)
    assert r.status_code == 200
    body = r.json()
    assert body["currency"] == "USD"
    assert body["predicted_price"] > 0


def test_predict_invalid_year(client):
    r = client.post("/predict", json={**VALID_CAR, "model_year": 1800})
    assert r.status_code == 422


def test_predict_negative_mileage(client):
    r = client.post("/predict", json={**VALID_CAR, "mileage": -5})
    assert r.status_code == 422


def test_predict_missing_field(client):
    bad = {k: v for k, v in VALID_CAR.items() if k != "brand"}
    r = client.post("/predict", json=bad)
    assert r.status_code == 422