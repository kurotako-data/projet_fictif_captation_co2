import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---- 1. Configuration de l'application ----
st.title("Projet Fictif : Développement d'un programme de crédits carbone basé sur la culture du chanvre")
st.markdown("""
**Contexte :**
La transition vers une économie bas-carbone nécessite l'intégration de solutions naturelles et innovantes pour capturer et compenser les émissions de CO₂. 
Le chanvre, grâce à ses capacités exceptionnelles de séquestration du carbone et ses co-bénéfices écologiques, représente une opportunité majeure.
Ce projet vise à développer un programme de crédits carbone autour de la culture du chanvre, intégrant des solutions biosourcées et circulaires.
""")

# ---- 2. Objectifs du projet ----
st.header("Objectifs du projet")
st.markdown("""
1. **Créer un programme de séquestration carbone :**
   - Développer des crédits carbone basés sur la capacité du chanvre à capturer le CO₂.
   - Soutenir les agriculteurs et industriels dans la mise en œuvre de pratiques agricoles régénératives.

2. **Maximiser les co-bénéfices écologiques :**
   - Préserver la biodiversité.
   - Améliorer la qualité des sols grâce à des techniques de culture régénératives.

3. **Développer des produits biosourcés innovants :**
   - Utiliser les dérivés du chanvre (biochar, béton de chanvre, bioplastiques) pour proposer des alternatives aux produits pétrochimiques.

4. **Contribuer à la stratégie Net Zéro :**
   - Proposer une solution naturelle et économique pour compenser les émissions résiduelles.
""")

# ---- 3. Paramètres utilisateur ----
st.sidebar.header("Paramètres")
# Entrées dynamiques de l'utilisateur
cout_implantation_par_hectare = st.sidebar.slider("Coût d’implantation par hectare (€)", 500, 5000, 1000)
prix_credit_carbone = st.sidebar.slider("Prix moyen d’un crédit carbone (€/tCO2)", 10, 200, 50)
superficie_min = st.sidebar.slider("Superficie minimale cultivée (ha)", 100, 1000, 100)
superficie_max = st.sidebar.slider("Superficie maximale cultivée (ha)", 1000, 10000, 5000, step=500)

# Calcul des paramètres dérivés
capture_CO2_par_hectare = 7  # Tonnes de CO2 capturées par hectare
hectares = np.arange(superficie_min, superficie_max + 500, 500)  # Superficie en hectares
revenu_par_hectare = capture_CO2_par_hectare * prix_credit_carbone

# ---- 4. Simulation des données ----
data = {
    "Hectares Cultivés": hectares,
    "Tonnes de CO2 Capturées": hectares * capture_CO2_par_hectare,
    "Revenu Crédit Carbone (€)": hectares * revenu_par_hectare,
    "Coût Total (€)": hectares * cout_implantation_par_hectare,
    "Bénéfice Net (€)": hectares * revenu_par_hectare - hectares * cout_implantation_par_hectare,
    "ROI (%)": (hectares * revenu_par_hectare - hectares * cout_implantation_par_hectare) / (hectares * cout_implantation_par_hectare) * 100
}

# Conversion en DataFrame
df = pd.DataFrame(data)

# ---- 5. Visualisation des résultats ----
st.header("Résultats Simulés")
st.markdown("""
Les graphiques ci-dessous montrent l'impact environnemental et économique du projet pour différents scénarios de superficie cultivée.
""")

# Graphique interactif 1 : Captation de CO2
st.subheader("Captation de CO2 en fonction de la surface cultivée")
fig, ax = plt.subplots()
ax.plot(df["Hectares Cultivés"], df["Tonnes de CO2 Capturées"], marker='o')
ax.set_title("Captation de CO2 en fonction de la surface cultivée")
ax.set_xlabel("Hectares cultivés")
ax.set_ylabel("CO2 capturé (tonnes)")
ax.grid()
st.pyplot(fig)

# Graphique interactif 2 : Bénéfice net et coût total
st.subheader("Coût total et bénéfice net en fonction de la surface cultivée")
fig, ax = plt.subplots()
ax.plot(df["Hectares Cultivés"], df["Coût Total (€)"], marker='o', label="Coût Total (€)", color="red")
ax.plot(df["Hectares Cultivés"], df["Bénéfice Net (€)"], marker='o', label="Bénéfice Net (€)", color="blue")
ax.set_title("Coût total et bénéfice net")
ax.set_xlabel("Hectares cultivés")
ax.set_ylabel("Montant (€)")
ax.legend()
ax.grid()
st.pyplot(fig)

# Tableau récapitulatif des résultats
st.subheader("Résumé des résultats simulés")
st.dataframe(df)

# ---- 6. Indicateurs de performance ----
st.header("Indicateurs de Performance Clés (KPI)")
st.markdown("""
- **Captation de CO₂ :** Tonnes de CO₂ capturées par hectare et par an.
- **Revenus générés :** Montant annuel issu des ventes de crédits carbone et de produits biosourcés.
- **Engagement des agriculteurs :** Nombre de partenariats agricoles conclus.
- **Co-bénéfices écologiques :** Indicateurs de biodiversité et régénération des sols.
""")

# ---- 7. Conclusion ----
st.header("Conclusion")
st.markdown("""
Ce projet met en avant l'importance de solutions naturelles telles que la culture du chanvre pour contribuer à la neutralité carbone.
En ajustant les paramètres, il est possible de maximiser les bénéfices économiques tout en répondant aux défis environnementaux. 
Cette méthodologie peut être étendue à d'autres cultures et secteurs pour un impact encore plus significatif.
""")

