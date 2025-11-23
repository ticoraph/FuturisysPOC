# Ce fichier définit les modèles de données (tables) pour SQLAlchemy.
# Elle permet à SQLAlchemy de savoir quelles classes représentent des tables
# et de gérer leur mapping avec la base de données (ORM - Object Relational Mapping).

from sqlalchemy import Column, Integer, Text, JSON, TIMESTAMP
from sqlalchemy.sql import func
from .session import class_base


class Prediction(class_base):
    """
    Table pour stocker l'historique des prédictions du modèle ML.
    Permet de tracer toutes les prédictions effectuées pour :
    - Analyser les performances du modèle
    - Faire du retraining avec de vraies données
    - Auditer les résultats
    """
    __tablename__ = "predictions"

    # Identifiant unique auto-incrémenté (clé primaire)
    id = Column(Integer, primary_key=True, index=True)

    # ID de la requête (permet de lier avec RequestLog)
    request_id = Column(Text, nullable=False)

    # Version du modèle utilisé pour cette prédiction
    # Important pour savoir quel modèle a produit quel résultat
    model_version = Column(Text)

    # Les données d'entrée (features) au format JSON
    # Stocke ce qui a été envoyé au modèle
    input_json = Column(JSON)

    # Le résultat de la prédiction au format JSON
    # Stocke ce que le modèle a retourné
    prediction_json = Column(JSON)

    # Temps d'exécution de la prédiction en millisecondes
    # Utile pour monitorer les performances du modèle
    latency_ms = Column(Integer)

    # Date et heure de création automatique (avec timezone)
    # server_default=func.now() signifie que PostgreSQL génère automatiquement la date
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


class RequestLog(class_base):
    """
    Table pour logger toutes les requêtes HTTP reçues par l'API.
    Permet de :
    - Tracer toutes les interactions avec l'API
    - Débugger les erreurs
    - Faire des statistiques d'utilisation
    - Auditer l'activité des utilisateurs
    """
    __tablename__ = "requests"

    # Identifiant unique auto-incrémenté (clé primaire)
    id = Column(Integer, primary_key=True, index=True)

    # ID de la requête (UUID généré dans l'API)
    # Permet de lier cette entrée avec la table Prediction
    request_id = Column(Text, nullable=False)

    # Identifiant de l'utilisateur qui a fait la requête (optionnel)
    # Peut être utilisé pour tracer qui utilise l'API
    user_id = Column(Text)

    # Le corps de la requête HTTP au format JSON
    # Stocke ce que l'utilisateur a envoyé
    payload = Column(JSON)

    # La réponse HTTP renvoyée au format JSON
    # Stocke ce que l'API a retourné (prédiction ou erreur)
    response = Column(JSON)

    # Code de statut HTTP (200 pour succès, 500 pour erreur, etc.)
    # Permet de filtrer rapidement les requêtes en erreur
    status_code = Column(Integer)

    # Date et heure de création automatique (avec timezone)
    # Timestamp de quand la requête a été reçue
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())