import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Especificações de GPU",
    page_icon="🖥️",
    layout="wide")

st.title("Página Inicial")

data_frame_gpu = pd.read_csv("datasets/gpu_specs_v7.csv")

marcas_gpu = data_frame_gpu['manufacturer'].unique()

marca_selecionada = st.sidebar.selectbox("Marca da GPU:", marcas_gpu)

df_gpu = data_frame_gpu[data_frame_gpu["manufacturer"]== marca_selecionada]


grafico_ano_lancamento = px.bar(
    df_gpu["releaseYear"].value_counts().reset_index(name="count"),
    x="releaseYear",  # Nome da coluna ajustada
    y="count",
    labels={"releaseYear": "Ano", "count": "Quantidade"},
    title=f"Distribuição de GPUs lançadas por ano - {marca_selecionada}"
)

st.dataframe(df_gpu)
st.plotly_chart(grafico_ano_lancamento)