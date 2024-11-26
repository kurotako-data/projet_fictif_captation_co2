# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---- 1. Simulation des données pour la culture du chanvre ----

# Paramètres de simulation
hectares = np.arange(100, 5000, 500)  # Superficie cultivée en hectares
capture_CO2_par_hectare = 7  # Tonnes de CO2 capturées par hectare
prix_credit_carbone = 50  # Prix moyen d'un crédit carbone en euros
revenu_par_hectare = capture_CO2_par_hectare * prix_credit_carbone  # Revenu par hectare en crédits carbone

# Simulation des données pour chaque hectare cultivé
data = {
    "Hectares Cultivés": hectares,
    "Tonnes de CO2 Capturées": hectares * capture_CO2_par_hectare,
    "Revenu Crédit Carbone (€)": hectares * revenu_par_hectare,
}

# Conversion en DataFrame
df = pd.DataFrame(data)

# ---- 2. Visualisation des résultats ----

# Graphique 1 : Captation totale de CO2 en fonction des hectares cultivés
plt.figure(figsize=(10, 6))
plt.plot(df["Hectares Cultivés"], df["Tonnes de CO2 Capturées"], marker='o')
plt.title("Captation de CO2 en fonction de la surface cultivée")
plt.xlabel("Hectares cultivés")
plt.ylabel("CO2 capturé (tonnes)")
plt.grid()
plt.show()

# Graphique 2 : Revenu généré par les crédits carbone en fonction des hectares cultivés
plt.figure(figsize=(10, 6))
plt.plot(df["Hectares Cultivés"], df["Revenu Crédit Carbone (€)"], marker='o', color="green")
plt.title("Revenu généré par les crédits carbone en fonction de la surface cultivée")
plt.xlabel("Hectares cultivés")
plt.ylabel("Revenu (€)")
plt.grid()
plt.show()

# ---- 3. Résumé chiffré des résultats ----
# Calcul des impacts économiques et environnementaux
total_co2_captured = df["Tonnes de CO2 Capturées"].sum()
total_revenue = df["Revenu Crédit Carbone (€)"].sum()

# Création d'un résumé
summary = pd.DataFrame({
    "Total CO2 Capturé (tonnes)": [total_co2_captured],
    "Revenu Total Crédit Carbone (€)": [total_revenue],
    "Superficie Moyenne Cultivée (ha)": [df["Hectares Cultivés"].mean()]
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Résumé des Résultats Simulés", dataframe=summary)

# ---- Détails supplémentaires et calculs ----

# Ajout d'autres données pour enrichir l'analyse
# Données simulées sur le coût d'implémentation (€/hectare)
cout_implantation_par_hectare = 1000  # Coût estimé pour mettre en place la culture de chanvre par hectare

# Calcul des coûts totaux
df["Coût Total (€)"] = df["Hectares Cultivés"] * cout_implantation_par_hectare

# Calcul des bénéfices nets
df["Bénéfice Net (€)"] = df["Revenu Crédit Carbone (€)"] - df["Coût Total (€)"]

# Ajout d'une colonne d'intensité carbone (en tonnes CO2/hectare)
# On considère que 7 tonnes capturées par hectare sont nettes après déduction des émissions liées à la production
df["Intensité Carbone (tonnes/ha)"] = capture_CO2_par_hectare

# ---- Visualisations supplémentaires ----

# Graphique 3 : Coût total et bénéfice net en fonction des hectares cultivés
plt.figure(figsize=(12, 6))
plt.plot(df["Hectares Cultivés"], df["Coût Total (€)"], marker='o', label="Coût Total (€)", color="red")
plt.plot(df["Hectares Cultivés"], df["Bénéfice Net (€)"], marker='o', label="Bénéfice Net (€)", color="blue")
plt.title("Coût total et bénéfice net en fonction des hectares cultivés")
plt.xlabel("Hectares cultivés")
plt.ylabel("Montant (€)")
plt.legend()
plt.grid()
plt.show()

# ---- Calcul des bénéfices environnementaux et économiques ----

# Résumé détaillé
summary_details = {
    "Total Hectares Cultivés": [df["Hectares Cultivés"].sum()],
    "Total CO2 Capturé (tonnes)": [df["Tonnes de CO2 Capturées"].sum()],
    "Revenu Total Crédit Carbone (€)": [df["Revenu Crédit Carbone (€)"].sum()],
    "Coût Total Implantation (€)": [df["Coût Total (€)"].sum()],
    "Bénéfice Net Total (€)": [df["Bénéfice Net (€)"].sum()],
    "Intensité Carbone Moyenne (tonnes/ha)": [df["Intensité Carbone (tonnes/ha)"].mean()]
}

# Conversion en DataFrame pour présentation
summary_details_df = pd.DataFrame(summary_details)

import ace_tools as tools; tools.display_dataframe_to_user(name="Résumé Détail des Résultats Simulés", dataframe=summary_details_df)
