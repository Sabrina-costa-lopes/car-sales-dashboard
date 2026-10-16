
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Análise de anúncios de veículos",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Análise de anúncios de veículos")
st.write(
    "Explore os preços e as características dos veículos anunciados."
)

# Carregar os dados
car_data = pd.read_csv("vehicles.csv")

st.write(f"Total de anúncios: {len(car_data):,}")

# Botão para criar histograma
if st.button("Criar histograma de preços"):
    st.subheader("Distribuição dos preços dos veículos")

    fig = px.histogram(
        car_data,
        x="price",
        title="Distribuição dos preços dos veículos",
        labels={"price": "Preço (US$)"},
        nbins=50
    )

    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
if st.button("Criar gráfico de dispersão"):
    st.subheader("Ano do modelo e preço")

    fig = px.scatter(
        car_data,
        x="model_year",
        y="price",
        title="Relação entre ano do modelo e preço",
        labels={
            "model_year": "Ano do modelo",
            "price": "Preço (US$)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)
