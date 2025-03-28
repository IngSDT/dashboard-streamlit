import streamlit as st
import pandas as pd

# Agregar un logo
st.image("logo_azul_transparencia2.png", width=150)  # Asegúrate de que "logo.png" está en la misma carpeta

# Título del dashboard
st.title("📊 Dashboard Para visualizar información con Carga de Archivos")

# Área para subir archivos
uploaded_file = st.file_uploader("📂 Selecciona un archivo", type=["csv", "xlsx"])

# Procesar el archivo subido
if uploaded_file is not None:
    st.success(f"✅ Archivo '{uploaded_file.name}' subido correctamente")

    # Si es un archivo CSV
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    # Si es un archivo Excel
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file, engine="openpyxl")

    # Mostrar los datos
    st.write("📌 Vista previa del archivo:")
    st.dataframe(df)
else:
    st.info("⚠️ Esperando que subas un archivo...")
