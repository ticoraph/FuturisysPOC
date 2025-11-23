from fastapi.testclient import TestClient
from  import api

client = TestClient(api)

def test_predict_ok():
    payload = {"x1": 1.0, "x2": 2.0}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    # Vérifie présence de la clé
    assert "prediction" in data
    # Vérifie que la valeur est numérique
    assert isinstance(data["prediction"], (int, float))


def test_predict_missing_field():
    payload = {"x1": 1.0}  # x2 manquant
    response = client.post("/predict", json=payload)

    # FastAPI renvoie 422 en cas de validation Pydantic ratée
    assert response.status_code == 422


def test_predict_invalid_type():
    payload = {"x1": "hello", "x2": 2.0}  # type incorrect
    response = client.post("/predict", json=payload)

    assert response.status_code == 422