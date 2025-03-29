import streamlit as st
from modules import visuel, audio, posture, indicateurs, dataset
import pandas as pd
import os

st.set_page_config(page_title='PsyAI', layout='wide')
st.title('🧠 PsyAI – Plateforme IA clinique complète')

menu = st.sidebar.radio("Navigation", [
    "Accueil",
    "Observation Visuelle",
    "Analyse Vocale",
    "Langage Corporel",
    "Indicateurs Cliniques",
    "Données Cliniques",
    "📈 Évolution Patient"
])

if menu == "Observation Visuelle":
    visuel.afficher()
elif menu == "Analyse Vocale":
    audio.afficher()
elif menu == "Langage Corporel":
    posture.afficher()
elif menu == "Indicateurs Cliniques":
    indicateurs.afficher()
elif menu == "Données Cliniques":
    dataset.afficher()
elif menu == "📈 Évolution Patient":
    st.subheader("📈 Suivi d'évolution clinique du patient")
    filepath = "data/sessions.csv"
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        patient_selection = st.selectbox("Choisir un patient :", df["nom"].unique())
        df_patient = df[df["nom"] == patient_selection]
        st.line_chart(df_patient.set_index("date")[[
            "clignements", "asymétrie_moyenne", "mouvement_sourcils_moyen"
        ]])
    else:
        st.warning("Aucune donnée disponible. Lancez une session d'observation pour enregistrer des données.")
else:
    st.markdown("""
    ## Bienvenue dans PsyAI
    Une plateforme d’analyse comportementale et clinique basée sur l’intelligence artificielle.
    Choisissez un module à gauche pour commencer. 🧠💬🧍
    """)