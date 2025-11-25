import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import time

# Exemple: entraîner un modèle simple (remplace par ton training)
data = load_iris()
X, y = data.data, data.target
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X, y)

# optionnel: ajouter attribut version
clf.version = f"rf-{int(time.time())}"

joblib.dump(clf, "model.joblib")