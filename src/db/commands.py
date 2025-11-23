# pip install python-dotenv sqlalchemy psycopg2

# Import moteur de connexion à la BDD + classe de base déclarative
from src.db.session import engine, class_base

# Importe le module schema qui contient les modèles de données
from src.db import models  # noqa: F401 - Enregistre les modèles auprès de SQLAlchemy

# crée physiquement toutes les tables dans la base de données.
class_base.metadata.create_all(bind=engine)

