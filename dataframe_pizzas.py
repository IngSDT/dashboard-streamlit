import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas de Pizzas", layout="wide")

st.title("Dashboard de Ventas por Categoría")

# Subir archivo CSV
#archivo = st.file_uploader("pizza_sales", type=["csv"])


    # Cargar el DataFrame
df = pd.read_csv("Dashboard/pizza_sales.csv")

    # Verificar que las columnas necesarias existen
if "pizza_category" in df.columns and "total_price" in df.columns:
        # Agrupar por categoría y sumar los precios
        data_agrupada = df.groupby("pizza_category")["total_price"].sum().reset_index()

        # Mostrar tabla de totales
        st.write("### Total de ventas por categoría")
        st.dataframe(data_agrupada)

        # Crear gráfico de barras
        fig = px.bar(
            data_agrupada,
            x="pizza_category",
            y="total_price",
            title="Total de Ventas por Categoría",
            labels={"total_price": "Total en $", "Categoria": "Categoría"},
            text_auto=True,
            color="pizza_category",
        )

        # Mostrar gráfico
        st.plotly_chart(fig, use_container_width=True)

else:
        st.error("El archivo debe contener las columnas 'Categoria' y 'total_price'.")
