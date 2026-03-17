import streamlit as st
import requests
import json

st.set_page_config(page_title="Iris ML Factory", page_icon="🌸")

st.title("🌸 Iris ML Factory : Serving Temps Réel")
st.write("Démonstration du **Hot-Reloading** (Zéro-Downtime)")

# Sidebar pour afficher l'état de l'infrastructure
st.sidebar.header("Statut Infrastructure")
st.sidebar.success("API: Connectée")
st.sidebar.info("Modèle : Iris Dataset")

# Formulaire de saisie pour les prédictions
st.subheader("Faire une prédiction")
col1, col2 = st.columns(2)
with col1:
    sepal_l = st.number_input("Sepal Length", value=5.1)
    sepal_w = st.number_input("Sepal Width", value=3.5)
with col2:
    petal_l = st.number_input("Petal Length", value=1.4)
    petal_w = st.number_input("Petal Width", value=0.2)

if st.button("Prédire"):
    payload = {"data": [[sepal_l, sepal_w, petal_l, petal_w]]}
    
    try:
        # On appelle ton API FastAPI
        response = requests.post("http://api:8000/predict", json=payload)
        result = response.json()

        if "error" in result:
            st.error(f"Erreur API : {result['error']}")
        else:
            # Affichage du résultat avec mise en valeur de la VERSION
            st.divider()
            st.balloons()

            c1, c2 = st.columns(2)
            c1.metric(label="Classe Prédite", value=result["prediction"][0])
            c2.metric(label="Version du Modèle", value=f"v{result['model_version']}")

            st.success(f"Prédiction effectuée avec succès malheuresement vous n'avez pas eu tous les bon numéros.")

    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {e}")

st.divider()
st.caption("Projet ML Factory - Traçabilité Totale activée.")