import pandas as pd
import streamlit as st
import plotly.express as px

datos = pd.read_csv("datos/vehicles_us.csv")

st.title("Análisis de Vehículos en Estados Unidos")

# Gráfico de distribución de tipos de vehículos
fig_tipo = px.histogram(
    datos, x="type", title="Distribución de Tipos de Vehículos")
st.plotly_chart(fig_tipo)
