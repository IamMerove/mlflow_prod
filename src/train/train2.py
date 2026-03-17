import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier   # ← Changement ici
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import os
from dotenv import load_dotenv

load_dotenv()

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Iris_ExperimentV2")

os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://localhost:9000"

def train_and_register():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    model_name = "iris_model"

    with mlflow.start_run() as run:
        # Modèle RandomForest pour la phase 2
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=None
        )
        model.fit(X_train, y_train)

        accuracy = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)
        print(f"Modèle RandomForest entraîné avec une précision de : {accuracy:.2f}")

        # Logs supplémentaires pour mieux comparer
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)
        mlflow.log_param("criterion", "gini")

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name=model_name
        )

        
        print("Modèle loggé et enregistré, mais alias Production NON modifié automatiquement.")

        client = MlflowClient()
        versions = client.get_latest_versions(model_name, stages=["None"])
        if versions:
            latest_version = versions[0].version
            print(f"Nouvelle version créée : {latest_version} (en attente d'attribution manuelle à Production)")

if __name__ == "__main__":
    train_and_register()