
import numpy as np
import pandas as pd
import joblib
from utils import transform_data

# Obtiene la ruta absoluta del directorio actual donde se encuentra este script


# Define la ruta completa del archivo de registro


# Configura el logger para que escriba en el archivo de registro especificado


def predict(input_data):
    try:
        # Convertir los datos de entrada a un DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Aplicar la función transform_data()
        transformed_df = transform_data(input_df)
        
        # Cargar el modelo
        model_rf = joblib.load('model_rf.joblib')
        
        # Realizar la predicción
        prediction = model_rf.predict(transformed_df)
                
        # Log para registrar la predicción realizada

        
        # Devolver el resultado de la predicción
        return {'prediction': int(prediction[0])}
    except Exception as e:
        return {'error': 'Error durante la predicción' +str(e)}