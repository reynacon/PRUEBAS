import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

#Primer histograma

# Crear la interfaz de usuario
st.title('Análisis de Vehículos')

# Sección: Histograma de Odómetro
st.header('Distribución del Odómetro')
if st.button('Mostrar histograma'):
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

#Segundo Grafico

# Sección: Comparación de Precios entre Fabricantes
st.header('Comparación de Precios por Fabricante')

# Selección de fabricantes
manufacturers = car_data['model'].unique()
manufacturer1 = st.selectbox('Seleccionar fabricante 1', manufacturers)
manufacturer2 = st.selectbox('Seleccionar fabricante 2', manufacturers)

# Normalizar el histograma
normalize = st.checkbox('Normalizar histograma')

if st.button('Comparar precios'):
    # Filtrar los datos según los fabricantes seleccionados
    filtered_data = car_data[(car_data['model'] == manufacturer1) | (car_data['model'] == manufacturer2)]
    
    # Crear el gráfico
    fig = px.histogram(filtered_data, x="price", color="model",
                       barmode='overlay',
                       histnorm='percent' if normalize else None,
                       title="Distribución de Precios por Fabricante")
    st.plotly_chart(fig, use_container_width=True)

#Grafico de dispersion

# Sección: Relación entre Precio y Kilometraje por Año y Tipo
st.header('Relación entre Precio y Kilometraje')

# Slider para seleccionar el rango de años
min_year = int(car_data['model_year'].min())
max_year = int(car_data['model_year'].max())
year_range = st.slider('Seleccionar rango de años', min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Selección de tipo de vehículo (opcional)
vehicle_types = car_data['type'].unique()
selected_type = st.selectbox('Seleccionar tipo de vehículo (opcional)', vehicle_types, index=len(vehicle_types)-1)  # Por defecto, seleccionar "Todos"

# Filtrar los datos según el rango de años y tipo de vehículo
filtered_data = car_data[(car_data['model_year'] >= year_range[0]) & 
                        (car_data['model_year'] <= year_range[1]) & 
                        (car_data['type'] == selected_type if selected_type != "Todos" else True)]

# Crear el gráfico de dispersión
fig = px.scatter(filtered_data, x='odometer', y='price', color='type',
                title=f'Relación entre precio y kilometraje para vehículos entre {year_range[0]} y {year_range[1]}',
                labels={'odometer': 'Kilometraje', 'price': 'Precio'})
st.plotly_chart(fig, use_container_width=True)

