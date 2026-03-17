ML Factory - Iris Prediction Service

Cette "Usine ML" automatise le cycle de vie d'un modèle de Machine Learning, de l'entraînement au serving, avec une gestion de mise à jour à chaud (Hot-Reloading) sans interruption de service.

🚀 Fonctionnalités
Infrastructure MLOps : Orchestration Docker-Compose (MLflow, MinIO, FastAPI, Streamlit).

Zéro-Downtime : L'API détecte dynamiquement le changement d'alias @prod dans MLflow.

Traçabilité : Chaque prédiction affiche la version exacte du modèle utilisé.

📂 Structure du projet
Plaintext
.
├── src/
│   ├── api/     # Service FastAPI (Serving)
│   ├── front/   # Interface Streamlit
│   └── train/   # Scripts d'entraînement (V1 & V2)
├── docker-compose.yml
├── .env.example   # Modèle de configuration
└── README.md
🛠️ Installation et Lancement
1. Configuration des variables d'environnement
C'est l'étape cruciale pour la liaison entre les services.

Bash
cp .env.example .env
Éditez le .env avec les accès suivants :

AWS_ACCESS_KEY_ID=minioadmin

AWS_SECRET_ACCESS_KEY=minioadmin

MLFLOW_S3_ENDPOINT_URL=http://localhost:9000 (pour l'hôte)

MLFLOW_TRACKING_URI=http://localhost:5000

2. Démarrage des services Docker
Bash
docker compose up -d --build
Accès : MLflow (:5000), MinIO (:9001), Streamlit (:8501), API (:8000).

3. Cycle d'entraînement (Hot-Reloading)
Phase 1 (V1) : Lancez uv run --env-file .env src/train/train.py. Cela crée le modèle et l'alias prod.

Test UI : Faites une prédiction sur Streamlit. Elle affiche v1.

Phase 2 (V2) : Lancez uv run --env-file .env src/train/train2.py.

Bascule : Une fois l'alias prod déplacé sur la V2 (via script ou UI MLflow), Streamlit affiche v2 instantanément sans redémarrer l'API.

🛡️ Débogage & Robustesse
Logs : docker compose logs -f api front pour suivre les échanges en temps réel.

Gestion d'erreur : Le Front Streamlit intercepte les dictionnaires {'error': '...'} si l'alias prod est manquant dans le registre, évitant ainsi un crash de l'interface.