import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Detalhes das GPU",
    page_icon="🖥️",
    layout="wide")

st.title("Especificações das GPU'S")

data_frame_gpu = pd.read_csv("datasets/gpu_specs_v7.csv")

data_frame_gpu["releaseYear"] = pd.to_numeric(data_frame_gpu["releaseYear"], errors="coerce")

data_frame_gpu = data_frame_gpu.dropna(subset=["releaseYear"])

data_frame_gpu["releaseYear"] = data_frame_gpu["releaseYear"].astype(int)

marcas_gpu = data_frame_gpu['manufacturer'].unique()

marca_selecionada = st.sidebar.selectbox("Marca da GPU:", marcas_gpu)

df_gpu = data_frame_gpu[data_frame_gpu["manufacturer"]== marca_selecionada]

gpus = df_gpu["productName"].unique()

nome_gpus = st.sidebar.selectbox("Nome da GPU", gpus)

df_especificacoes = data_frame_gpu[data_frame_gpu["productName"] == nome_gpus]

nome_da_gpu = df_especificacoes["productName"].iloc[0]
ano_da_gpu = df_especificacoes["releaseYear"].iloc[0]
memoria_da_gpu = f"{df_especificacoes["memSize"].iloc[0]}GB"
tipo_da_gpu = df_especificacoes["memType"].iloc[0]

st.title(nome_da_gpu)
st.subheader(ano_da_gpu)

coluna_1, coluna_2 = st.columns(2)

coluna_1.metric("Memória da GPU", memoria_da_gpu)
coluna_2.metric("Tipo da GPU", tipo_da_gpu)

st.divider()