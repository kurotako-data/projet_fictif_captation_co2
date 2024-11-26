import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---- 1. Configuration de l'application ----
st.title("Analyse interactive : Impact environnemental et économique de la culture du chanvre")
st.markdown("""
Cette application vous permet d'explorer les impacts économiques et environnementaux d'un programme de crédits carbone basé sur la culture du chanvre.
Modifiez les paramètres pour analyser les scénarios en temps réel.
""")

# ---- 2. Paramètres utilisateur ----
st.sidebar.header("Paramètres")
# Entrées dynamiques de l'utilisateur
cout_implantation_par_hectare = st.sidebar.slider("Coût d'implantation par hectare (€)", 500, 5000, 1000)
prix_credit_carbone = st.sidebar.slider("Prix moyen d'un crédit carbone (€/tCO2)", 10, 200, 50)
superficie_min = st.sidebar.slider("Superficie minimale cultivée (ha)", 100, 1000, 100)
superficie_max = st.sidebar.slider("Superficie maximale cultivée (ha)", 1000, 10000, 5000, step=500)

# Calcul des paramètres dérivés
capture_CO2_par_hectare = 7  # Tonnes de CO2 capturées par hectare
hectares = np.arange(superficie_min, superficie_max + 500, 500)  # Superficie en hectares
revenu_par_hectare = capture_CO2_par_hectare * prix_credit_carbone

# ---- 3. Simulation des données ----
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

# ---- 4. Visualisation des résultats ----
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

# ---- 5. Scénarios de prix des crédits carbone ----
st.sidebar.header("Scénarios de prix")
prix_scenarios = st.sidebar.multiselect("Sélectionnez les prix des crédits carbone à comparer (€/tCO2)", [30, 50, 100], default=[30, 50, 100])

if prix_scenarios:
    revenus_scenarios = {}
    for prix in prix_scenarios:
        revenus_scenarios[f"Revenu pour {prix}€/tCO2"] = hectares * capture_CO2_par_hectare * prix

    scenarios_df = pd.DataFrame(revenus_scenarios, index=hectares)
    scenarios_df.index.name = "Hectares Cultivés"

    # Graphique interactif : Scénarios de prix
    st.subheader("Revenus estimés selon différents prix des crédits carbone")
    fig, ax = plt.subplots()
    for prix in prix_scenarios:
        ax.plot(hectares, scenarios_df[f"Revenu pour {prix}€/tCO2"], label=f"{prix} €/tCO2")
    ax.set_title("Revenus estimés selon différents prix des crédits carbone")
    ax.set_xlabel("Hectares cultivés")
    ax.set_ylabel("Revenus (€)")
    ax.legend()
    ax.grid()
    st.pyplot(fig)

# ---- 6. Conclusion ----
st.markdown("""
### Conclusion
Cette application interactive met en évidence l'impact économique et environnemental de la culture du chanvre pour des crédits carbone. 
Les résultats montrent comment ajuster les coûts, les prix des crédits carbone et la surface cultivée peut maximiser les bénéfices nets et réduire l'empreinte carbone.
""")
