import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import os
from dotenv import load_dotenv

load_dotenv()

# Je configure la connexion a Mlflow
# Comme on lance le script depuis l'hote on utilise localhost

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Iris_Experiment")
# FORCE l'adresse que MLflow va donner aux autres services
os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://localhost:9000" 
# Note : Pour l'API, on devra s'assurer qu'elle utilise 'http://minio:9000'
# Je créer la fonction

def train_and_register():
    # On charge les données Iris
    iris=load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # On choisi le nom du modele dans le registre
    model_name= "iris_model"

    with mlflow.start_run() as run:
        #Entrainement de la phase 1 : Regression Logistique
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        # Calcul d'une metrique simple
        accuracy= model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)
        print(f"Modele entrainé avec une précision de : {accuracy: .2f}")

        # On enregistre le modele dans le registre
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name=model_name
        )

        # Phase 1 du brief, passage en force, Automation
        # On récupere la derniere version qu'on vient de créer
        client = MlflowClient()
        versions = client.get_latest_versions(model_name, stages=["None"])
        latest_version = versions[0].version
        # On pousse l'alias "Production" sur cette version
        client.set_registered_model_alias(model_name, "Production", latest_version)
        print(f"✅ Version {latest_version} du modèle '{model_name}' passée en Production.")


if __name__ == "__main__":
    train_and_register()