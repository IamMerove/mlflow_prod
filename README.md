# 🌸 ML Factory - Iris Prediction Service

Cette "Usine ML" automatise le cycle de vie d'un modèle de Machine Learning, de l'entraînement au serving, avec une gestion de mise à jour à chaud (**Hot-Reloading**) sans interruption de service.

## 🚀 Fonctionnalités
- **Infrastructure MLOps** : Orchestration Docker-Compose (MLflow, MinIO, FastAPI, Streamlit).
- **Expérimentation** : Versionnage automatique des modèles (V1: LogReg, V2: RandomForest).
- **Zéro-Downtime** : L'API détecte dynamiquement le changement d'alias "Production" dans le registre MLflow.
- **Interface UI** : Test des prédictions en temps réel avec affichage de la version du modèle.

## 📂 Structure du projet
```text
.
├── src/
│   ├── api/     # Service FastAPI (Serving)
│   ├── front/   # Interface Streamlit
│   └── train/   # Script d'entraînement et de packaging
├── docker-compose.yml
├── .env.example
└── README.md
🛠️ Installation et Lancement
1. Prérequis
Docker & Docker Compose

Python 3.10+ (ou uv)

2. Configuration
Copiez le fichier d'exemple et remplissez vos variables :

Bash
cp .env.example .env
3. Lancement de l'infrastructure
Bash
docker compose up -d
Accès aux outils :

MLflow UI : http://localhost:5000

MinIO UI : http://localhost:9001

4. Entraînement et Déploiement
Pour entraîner le modèle et le pousser en production :

Bash
uv run --env-file .env src/train/train.py
uv run --env-file .env src/train/train2.py

5. Lancement de l'interface utilisateur
Bash
uv run streamlit run src/front/app.py

📊 Démonstration du Hot-Reloading
Effectuez une prédiction sur le Front (Version 1 affichée).

Modifiez le modèle dans train.py (ex: passage à RandomForest).

Relancez le script d'entraînement.

Refaites une prédiction sur le Front : la Version 2 apparaît instantanément sans redémarrage des services.

🛡️ Traçabilité
Chaque réponse de l'API contient le champ model_version pour assurer une correspondance totale entre la prédiction et l'expérience enregistrée dans MLflow.