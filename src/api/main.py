from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
import os
from dotenv import load_dotenv
from mlflow.tracking import MlflowClient

load_dotenv()

app = FastAPI(title="The ML Factory API")

class IrisRequest(BaseModel):
    data: list

# ──────────────────────────────────────────────────────────────
# ALIAS UTILISÉ : "prod" (minuscule, sans espace)
# ──────────────────────────────────────────────────────────────
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000"))
model_uri = "models:/iris_model@prod"

client = MlflowClient()

@app.get("/")
def read_root():
    return {"status": "Factory is running", "model_uri": model_uri}

@app.post("/predict")
def predict(request: IrisRequest):
    try:
        # Chargement du modèle via l'alias
        model = mlflow.pyfunc.load_model(model_uri)
        
        df = pd.DataFrame(request.data)
        
        prediction = model.predict(df)
        
        # Récupération de la version via le même alias
        model_version_obj = client.get_model_version_by_alias("iris_model", "prod")
        version = model_version_obj.version
        
        return {
            "prediction": prediction.tolist(),
            "model_version": version
        }
    
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")