from fastapi.testclient import TestClient
from src.start import api

client = TestClient(api)


def test_predict_ok():
    """Test d'une prédiction réussie avec des features valides"""
    payload = {"features": [1, 2, 3, 4]}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    # Vérifie la présence de toutes les clés attendues
    assert "prediction" in data
    assert "request_id" in data
    assert "model_version" in data
    assert "latency_ms" in data

    # Vérifie les types
    assert isinstance(data["request_id"], str)
    assert isinstance(data["model_version"], str)
    assert isinstance(data["latency_ms"], int)
    # La prédiction peut être de différents types selon le modèle
    assert data["prediction"] is not None


def test_predict_missing_field():
    """Test avec le champ 'features' manquant"""
    payload = {"x1": 1.0}  # Mauvaise structure
    response = client.post("/predict", json=payload)

    # FastAPI renvoie 422 en cas de validation Pydantic ratée
    assert response.status_code == 422


def test_predict_invalid_type():
    """Test avec des types invalides dans les features"""
    payload = {"features": ["hello", 2.0]}  # Type string au lieu de float
    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_empty_features():
    """Test avec une liste de features vide"""
    payload = {"features": []}
    response = client.post("/predict", json=payload)

    # Peut retourner 422 ou 500 selon la validation du modèle
    assert response.status_code in [422, 500]


def test_predict_single_feature():
    """Test avec une seule feature"""
    payload = {"features": [5.5]}
    response = client.post("/predict", json=payload)

    # Le modèle peut accepter ou rejeter selon ses attentes
    assert response.status_code in [200, 500]


def test_health_endpoint():
    """Test de l'endpoint de santé"""
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "ok"


def test_model_endpoint():
    """Test de l'endpoint de vérification du modèle"""
    response = client.get("/model")

    assert response.status_code == 200
    data = response.json()
    assert "model_loaded" in data
    assert isinstance(data["model_loaded"], bool)