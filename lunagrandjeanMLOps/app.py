import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from prometheus_client import Counter, start_http_server

# Démarrer un serveur HTTP pour exposer les métriques à Prometheus
start_http_server(8000)

# Initialiser un compteur Prometheus
data_view_counter = Counter('data_views', 'Nombre de fois que les données brutes ont été visualisées')

# Charger le jeu de données
@st.cache
def load_data():
    df = pd.read_csv("housing.csv")
    return df

df = load_data()

# Titre de l'application web
st.title("California Housing Statistics")

# Montrer le jeu de données
if st.checkbox('Show raw data'):
    data_view_counter.inc()  # Incrémenter le compteur quand les données brutes sont affichées
    st.subheader('Raw Data')
    st.write(df.head())

# Afficher des statistiques simples
st.subheader('Basic Statistics')
st.write(df.describe())

# Map of Housing Locations
st.subheader("Map of Housing Locations")
fig, ax = plt.subplots()
df.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
        s=df["population"]/100, label="Population", figsize=(10,7),
        c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, ax=ax)
plt.legend()
st.pyplot(fig)

# Histogramme de l'âge médian des logements
st.subheader("Distribution of Housing Median Age")
fig, ax = plt.subplots()
sns.histplot(df['housing_median_age'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Bar Plot for Median Income
st.subheader("Median Income Distribution")
fig, ax = plt.subplots()
sns.barplot(x="ocean_proximity", y="median_income", data=df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Graphique de dispersion pour la valeur médiane des maisons vs revenu médian
st.subheader("Median House Value vs. Median Income")
fig, ax = plt.subplots()
sns.scatterplot(x='median_income', y='median_house_value', hue='ocean_proximity', data=df, ax=ax)
plt.xlabel("Median Income (tens of thousands)")
plt.ylabel("Median House Value")
st.pyplot(fig)
