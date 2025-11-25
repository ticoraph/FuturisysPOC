from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Any
import numpy as np
import uuid
from src.model.load_model import LoadModel
from src.db.session import session_local
from src.db.models import Prediction, RequestLog

# Définition de la version de l'API
version = "v1"

# Création de l'application FastAPI avec ses métadonnées
api = FastAPI(
    title="FastAPI Backend",
    description="Backend for Python-PostgreSQL setup",
    version=version
)

# Instanciation du modèle de machine learning (chargé une seule fois au démarrage)
load_model = LoadModel()

##################################
# DÉFINITION DES SCHÉMAS DE DONNÉES (Pydantic Models)
##################################

class PredictRequest(BaseModel):
    """
    Schéma pour les données d'entrée de la prédiction.
    Attend une liste de valeurs numériques (features) pour faire la prédiction.
    """
    features: List[float] = Field(
        ...,
        min_length=4,
        examples=[[1, 2, 3, 4]]
    )

class PredictResponse(BaseModel):
    """
    Schéma pour la réponse de la prédiction.
    Retourne l'ID de la requête, la version du modèle, la prédiction et le temps d'exécution.
    """
    request_id: str
    model_version: str
    prediction: Any
    latency_ms: int

##################################
# ENDPOINTS DE L'API
##################################

@api.get("/health")
def health():
    """
    Endpoint de vérification de santé de l'API.
    Permet de vérifier que le serveur est opérationnel.
    """
    return {"status": "ok", }


@api.get("/model")
def model():
    """
    Endpoint pour vérifier si le modèle ML est correctement chargé en mémoire.
    Retourne True si le modèle est chargé, False sinon.
    """
    return {"model_loaded": load_model._model is not None}


@api.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    """
    Endpoint principal pour effectuer des prédictions.

    Processus :
    1. Génère un ID unique pour tracer la requête
    2. Convertit les features en array NumPy
    3. Fait la prédiction avec le modèle ML
    4. Enregistre tout dans la base de données (logs + prédictions)
    5. Retourne la prédiction avec ses métadonnées
    """

    # Génération d'un identifiant unique pour cette requête
    request_id = str(uuid.uuid4())

    # Transformation des features en format NumPy (attendu par le modèle)
    X = np.array([req.features])

    try:
        # Appel du modèle pour obtenir la prédiction et le temps d'exécution
        pred, latency = load_model.predict(X)
    except Exception as e:
        # En cas d'erreur lors de la prédiction :
        # - Enregistre l'erreur dans la table RequestLog
        # - Retourne une erreur HTTP 500 au client
        with session_local() as db:
            db.add(RequestLog(
                request_id=request_id,
                payload=req.dict(),
                response={"error": str(e)},
                status_code=500
            ))
            db.commit()
        raise HTTPException(status_code=500, detail=str(e))

    # Si la prédiction réussit, enregistrement dans la base de données :
    with session_local() as db:
        # 1. Log de la requête dans RequestLog (pour audit/monitoring)
        db.add(RequestLog(
            request_id=request_id,
            payload=req.dict(),
            response={"prediction": pred},
            status_code=200
        ))

        # 2. Sauvegarde de la prédiction dans la table Prediction (pour historique)
        db.add(Prediction(
            request_id=request_id,
            model_version=load_model.model_version,
            input_json=req.dict(),
            prediction_json={"prediction": pred},
            latency_ms=latency
        ))

        # Validation des changements en base de données
        db.commit()

    # Retour de la réponse au client avec toutes les informations
    return PredictResponse(
        request_id=request_id,
        model_version=load_model.model_version,
        prediction=pred,
        latency_ms=latency
    )
