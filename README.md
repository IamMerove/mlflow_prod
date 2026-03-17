
# Titre : 🌸 Iris ML Factory


Description :

Une infrastructure MLOps complète orchestrée par Docker, conçue pour l'entraînement, le versioning et le serving dynamique de modèles de Machine Learning. Ce projet démontre une architecture de Hot-Reloading permettant des mises à jour de modèles sans interruption de service.


## Badges
![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MLflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=mlflow&logoColor=blue)


## Deployment

Le projet repose sur une orchestration de 4 services isolés :

- **🧠 MLflow Server** : Gestion du registre de modèles et des expérimentations.
- **📦 MinIO (S3)** : Stockage des artifacts (fichiers .pkl) pour un découplage total.
- **🚀 FastAPI** : Serveur de prédiction haute performance qui interroge dynamiquement le registre.
- **🎨 Streamlit** : Interface utilisateur réactive affichant la version du modèle en temps réel.


## Environment Variables

Variable,Valeur par défaut,Description

AWS_ACCESS_KEY_ID=minioadmin (Login de l'interface MinIO)
AWS_SECRET_ACCESS_KEY=minioadmin (Password de l'interface MinIO)
MLFLOW_S3_ENDPOINT_URL=http://localhost:9000 (Point d'entrée pour le stockage des modèles)
MLFLOW_TRACKING_URI=http://localhost:5000 (Connexion au registre de modèles)


## Installation

# 1. Cloner le projet
git clone [URL_DU_DEPOT]
cd iris-ml-factory

# 2. Configurer les variables d'environnement
cp .env.example .env

# 3. Lancer l'infrastructure (Docker)
docker compose up -d --build
    
## Usage/Examples

### Phase 1 : Entraînement Initial
Lancez l'entraînement de la V1 (Logistic Regression) :
```bash
uv run --env-file .env src/train/train.py
```
### Phase 2 : Mise à jour dynamique (Hot-Reloading)
Lancez l'entraînement de la V2 (Random Forest) :

uv run --env-file .env src/train/train2.py


L'API détecte le changement d'alias. Rafraîchissez l'interface Streamlit pour voir la V2 en action sans redémarrage.

### A. Tech Stack
*(Dans cette tuile, sélectionne les logos ou liste-les simplement comme ceci)* :
- **Backend :** Python 3.10+, FastAPI, Uvicorn.
- **Frontend :** Streamlit.
- **MLOps :** MLflow, MinIO (S3-compliant).
- **DevOps :** Docker, Docker-Compose.
- **Gestionnaire de paquets :** UV.

---

### B. Lessons Learned 
**Contenu :**
```markdown
Ce projet a permis de valider des concepts critiques d'ingénierie ML :
- **Le découplage** : Séparer le code de l'API des fichiers de modèles pour faciliter la scalabilité.
- **L'abstraction** : Utiliser des alias (`@prod`) plutôt que des IDs de version fixes pour permettre des rollbacks instantanés.
- **La robustesse** : Gérer les erreurs de connexion entre services dans un réseau Docker.

------------------------------------------------------------------
### Tech Stack

**Cœur du Système :**
* **Langage :** Python 3.10+ (Gestion via **uv**)
* **API :** FastAPI & Uvicorn (Asynchrone & Haute performance)
* **Interface :** Streamlit (UI réactive)

**Infrastructure & MLOps :**
* **Conteneurisation :** Docker & Docker Compose
* **Registre de modèles :** MLflow
* **Stockage S3 :** MinIO
* **Base de données :** SQLite (Persistance des métadonnées)

**Science des données :**
* **ML Library :** Scikit-Learn (Logistic Regression & Random Forest)
* **Data :** Pandas & NumPy
--------------------------------------------------------------------
## Support

### 👤 Auteur
**[Sebastien IamMerove]**

