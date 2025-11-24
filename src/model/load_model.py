import joblib
import os
import time
#from typing import Any
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupère le chemin du modèle depuis les variables d'environnement
# Si MODEL_PATH n'existe pas, utilise "model.joblib" par défaut
model_path = os.getenv("model_path", "model.joblib")
print(f"Loading model from {model_path}")

# Affichage d'informations de débogage pour vérifier les chemins
print(f"Current working directory: {os.getcwd()}")
print(f"Model path from env: {os.getenv('model_path')}")
print(f"Absolute model path: {os.path.abspath(model_path)}")
print(f"File exists: {os.path.exists(model_path)}")


class LoadModel:
    """
    Classe responsable du chargement et de l'utilisation du modèle de machine learning.
    Elle gère le cycle de vie du modèle : chargement, versioning et prédictions.
    """

    def __init__(self, model_path: str = model_path):
        """
        Initialise la classe et charge automatiquement le modèle.

        Args:
            model_path: Chemin vers le fichier du modèle sauvegardé (format joblib)
        """
        self.model_path = model_path
        self._model = None  # Le modèle sera stocké ici une fois chargé
        self.model_version = None  # Version du modèle pour le tracking
        self.load_model()  # Charge le modèle immédiatement à l'instanciation

    def load_model(self):
        """
        Charge le modèle depuis le disque en utilisant joblib.
        Détermine également la version du modèle pour le suivi des versions.
        """
        # Chargement du modèle depuis le fichier joblib
        self._model = joblib.load(self.model_path)

        # Tentative de récupération de la version du modèle :
        # 1. Si le modèle a un attribut "version", on l'utilise
        # 2. Sinon, on utilise le timestamp de dernière modification du fichier
        self.model_version = getattr(
            self._model,
            "version",
            str(os.path.getmtime(self.model_path))
        )

    def predict(self, X):
        """
        Effectue une prédiction avec le modèle chargé.
        Mesure également le temps d'exécution (latence).

        Args:
            X: Les données d'entrée (features) au format NumPy array

        Returns:
            tuple: (prédictions, latence_en_ms)
                - prédictions: Liste des prédictions (probabilités ou classes)
                - latence_en_ms: Temps d'exécution en millisecondes
        """
        # Si le modèle n'est pas chargé, on le charge
        if self._model is None:
            self.load_model()

        # Début du chronomètre pour mesurer la latence
        start = time.time()

        # Tentative de prédiction avec gestion de différents types de modèles
        try:
            # Si le modèle supporte predict_proba (classification avec probabilités)
            # on l'utilise pour obtenir les probabilités de chaque classe
            if hasattr(self._model, "predict_proba"):
                y = self._model.predict_proba(X).tolist()
            else:
                # Sinon, on utilise predict classique (régression ou classification simple)
                y = self._model.predict(X).tolist()
        except Exception:
            # En cas d'erreur (par exemple si predict_proba échoue),
            # on se rabat sur predict standard
            y = self._model.predict(X).tolist()

        # Calcul de la latence en millisecondes
        latency_ms = int((time.time() - start) * 1000)

        # Retourne les prédictions et le temps d'exécution
        return y, latency_ms