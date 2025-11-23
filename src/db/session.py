# Gère la connexion à la base de données et la gestion des sessions SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupération des variables de connexion à PostgreSQL
USER = os.getenv("user")          # Nom d'utilisateur PostgreSQL
PASSWORD = os.getenv("password")  # Mot de passe PostgreSQL
HOST = os.getenv("host")          # Adresse du serveur (ex: localhost ou IP distante)
PORT = os.getenv("port")          # Port PostgreSQL (généralement 5432)
DBNAME = os.getenv("dbname")      # Nom de la base de données

# Construction de l'URL de connexion SQLAlchemy
# Format: postgresql+psycopg2://utilisateur:motdepasse@hote:port/nombase
# psycopg2 est le driver PostgreSQL utilisé par SQLAlchemy
# sslmode=require force la connexion SSL (sécurisée)
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Création du moteur de base de données (engine)
# C'est le point d'entrée principal pour interagir avec PostgreSQL
engine = create_engine(
    DATABASE_URL,
    future=True,  # Active le mode SQLAlchemy 2.0 (nouvelle API)
    connect_args={"sslmode": "require"}  # Force SSL pour la sécurité
)

# Création d'une factory de sessions
# session_local() va créer des sessions de base de données pour effectuer des opérations
# - autoflush=False : Ne flush pas automatiquement avant chaque requête
# - autocommit=False : Les transactions doivent être commitées manuellement
# - future=True : Utilise le style SQLAlchemy 2.0
session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# Classe de base pour tous les modèles ORM
# Tous les modèles de données (comme Prediction, RequestLog) vont hériter de cette classe
# Cela permet à SQLAlchemy de savoir qu'ils représentent des tables
class_base = declarative_base()

# Test de la connexion à la base de données au démarrage
try:
    with engine.connect() as connection:
        print("Connection successful!")  # Connexion réussie
except Exception as e:
    print(f"Failed to connect: {e}")  # Affiche l'erreur si la connexion échoue