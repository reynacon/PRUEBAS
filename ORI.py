import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Venta de Vehiculos')        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
            st.write('Construir un histograma para la columna price')
                # crear un histograma
            fig = px.histogram(car_data, x="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

        # Crear una lista de fabricantes únicos
manufacturers = car_data['model'].unique()

# Crear la interfaz de usuario
st.header('Comparación de precios entre fabricantes')

# Selección de fabricantes
manufacturer1 = st.selectbox('Seleccionar fabricante 1', manufacturers)
manufacturer2 = st.selectbox('Seleccionar fabricante 2', manufacturers)

# Normalizar el histograma
normalize = st.checkbox('Normalizar histograma')

# Crear el histograma
if st.button('Construir histograma'):
    # Filtrar los datos según los fabricantes seleccionados
    filtered_data = car_data[(car_data['model'] == manufacturer1) | 
                             (car_data['model'] == manufacturer2)]
    
    # Crear el gráfico
    fig = px.histogram(filtered_data, x="price", color="manufacturer",
                      barmode='overlay',
                      histnorm='percent' if normalize else None)
    
    # Personalizar el gráfico
    fig.update_layout(
        title="Distribución de precios por fabricante",
        xaxis_title="Precio",
        yaxis_title="Porcentaje"
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
