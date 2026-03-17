# On utilise une image légère
FROM python:3.10-slim

# Installation des dépendances système nécessaires pour les clients S3
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# On copie d'abord les dépendances pour profiter du cache Docker
COPY pyproject.toml .
RUN pip install --no-cache-dir fastapi uvicorn mlflow pandas boto3 scikit-learn python-multipart python-dotenv

# Copie du code de l'API
COPY src/api/main.py ./main.py

# L'API doit pouvoir parler à MLflow et MinIO
# On expose le port 8000
EXPOSE 8000

CMD ["python", "main.py"]