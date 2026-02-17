import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Cuadro de Mandos: Análisis de Vehículos')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creando un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para el gráfico de dispersión
build_scatter = st.button('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creando un gráfico de dispersión: Odómetro vs Precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
