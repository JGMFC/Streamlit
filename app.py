import streamlit as st
from api import predict  # Asegúrate de que la ruta es correcta según tu estructura de proyecto

# Configuración de Streamlit
st.title('¿Es probable que se cumpla?:')

# Formulario de entrada de Streamlit
IMPORTE_PROPUESTA = st.number_input("Importe Propuesta", 0.0)
TIPO_PROPUESTA = st.selectbox("Tipo propuesta", ['PROMESA', 'CAL_PAGO'])
PROP_VINCULADA = st.selectbox("Propuesta vinculada", ['NO','QUITA'])
PORCENTAJE_QUITA = st.slider("Porcentaje de Quita", 0, 70)
DEUDA_INICIAL = st.number_input("Deuda Inicial", 0.0)
DIAS_IMPAGO = st.number_input("Dias de impago", 0, 7500)
PRODUCTO_AGRUPADO = st.selectbox("Tipo producto", ['consumo', 'empresas', 'hipotecas', 'resto'])
REL_PER_CUE = st.selectbox("Tipo relacion", ['TIT', 'AVA', 'OTROS'])
MARCA_IND_SME = st.selectbox("Tipo de cliente", ['INDIVIDUALS', 'SME', 'SECURED'])
JUDICIALIZADO = st.selectbox("Judicializado", ['NO','SI'])

# Botón de predicción
if st.button('Predicción'):
    input_data = {
        'IMPORTE_PROPUESTA': IMPORTE_PROPUESTA,
        'TIPO_PROPUESTA': TIPO_PROPUESTA,
        'PROP_VINCULADA': PROP_VINCULADA,
        'PORCENTAJE_QUITA': PORCENTAJE_QUITA,
        'DEUDA_INICIAL': DEUDA_INICIAL,
        'DIAS_IMPAGO': DIAS_IMPAGO,
        'PRODUCTO_AGRUPADO': PRODUCTO_AGRUPADO,
        'REL_PER_CUE': REL_PER_CUE,
        'MARCA_IND_SME': MARCA_IND_SME,
        'JUDICIALIZADO': JUDICIALIZADO
    }
    
    # Llamar a la función predict y obtener el resultado
    result = predict(input_data)
    
    # Mostrar el resultado
    if 'error' in result:
        st.error('Error al realizar la predicción')
    else:
        if result['prediction'] == 1:
            st.success('Es probable que cumpla :thumbsup:')
        else:
            st.error('Es improbable que cumpla :thumbsdown:')