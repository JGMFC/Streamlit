FROM python:3.11.2-slim

# Exponer el puerto 8501
EXPOSE 8080 

# Actualizar pip
RUN pip install -U pip

# Copiar el archivo requirements.txt e instalar las dependencias
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copiar todo el contenido del directorio actual a /app y establecer el directorio de trabajo
COPY . /app
WORKDIR /app

# Ejecutar Streamlit en el puerto 8501 y en todas las interfaces de red
CMD streamlit run app.py --server.port 8080 --server.address 0.0.0.0