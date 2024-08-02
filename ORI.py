import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear la interfaz de usuario
st.header('Venta de Vehículos')

# Primer histograma: Odómetro
if st.button('Construir histograma de odómetro', key='hist_odometer'):
    fig = px.histogram(car_data, x="odometer", title="Distribución de Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Segundo histograma: Precio por fabricante
st.header('Comparación de precios entre fabricantes')

# Selección de fabricantes
manufacturers = car_data['model'].unique()
manufacturer1 = st.selectbox('Seleccionar fabricante 1', manufacturers)
manufacturer2 = st.selectbox('Seleccionar fabricante 2', manufacturers)

# Normalizar el histograma
normalize = st.checkbox('Normalizar histograma')

# Crear el histograma
if st.button('Construir histograma de precios', key='hist_price'):
    # Filtrar los datos según los fabricantes seleccionados
    filtered_data = car_data[(car_data['model'] == manufacturer1) | 
                             (car_data['model'] == manufacturer2)]
    
    # Crear el gráfico
    fig = px.histogram(filtered_data, x="price", color="model",
                      barmode='overlay',
                      histnorm='percent' if normalize else None,
                      title="Distribución de Precios por Fabricante")

#Tercer Histograma: Relación entre precio y modelo por tipo de vehículo
st.header('Relación entre precio y modelo por tipo de vehículo')
# Crear el gráfico de barras apiladas
fig = px.scatter(car_data, x="model", y="price", color="type",
                 title="Relación entre precio y modelo por tipo de vehículo")

# Mostrar el gráfico
st.plotly_chart(fig, use_container_width=True)
