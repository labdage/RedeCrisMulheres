
import streamlit as st
import pandas as pd

st.set_page_config(page_title='RedeCRIS Mulher', layout='wide')

# Título e introdução
st.markdown("<h1 style='color:#6a1b9a;'>RedeCRIS Mulher</h1>", unsafe_allow_html=True)
st.markdown("### Conectando dados, pesquisas e políticas no enfrentamento à violência de gênero")

# Carregar base
df = pd.read_csv('base_geral.csv')

# Filtros laterais
st.sidebar.header("Filtros")

grupo = st.sidebar.selectbox("Grupo", ['Todos'] + sorted(df['Grupo'].dropna().unique()))
pesquisador = st.sidebar.selectbox("Pesquisador(a)", ['Todos'] + sorted(df['Pesquisador'].dropna().unique()))
instituicao = st.sidebar.selectbox("Instituição", ['Todas'] + sorted(df['Instituicao'].dropna().unique()))
tipo = st.sidebar.selectbox("Tipo de Produção", ['Todos'] + sorted(df['Tipo'].dropna().unique()))
tema = st.sidebar.selectbox("Tema", ['Todos'] + sorted(df['Tema'].dropna().unique()))
ano = st.sidebar.selectbox("Ano", ['Todos'] + sorted(df['Ano'].dropna().astype(str).unique()))

# Aplicar filtros
filtro = df.copy()
if grupo != 'Todos':
    filtro = filtro[filtro['Grupo'] == grupo]
if pesquisador != 'Todos':
    filtro = filtro[filtro['Pesquisador'] == pesquisador]
if instituicao != 'Todas':
    filtro = filtro[filtro['Instituicao'] == instituicao]
if tipo != 'Todos':
    filtro = filtro[filtro['Tipo'] == tipo]
if tema != 'Todos':
    filtro = filtro[filtro['Tema'] == tema]
if ano != 'Todos':
    filtro = filtro[filtro['Ano'].astype(str) == ano]

# Exibir resultados
st.markdown("### Resultados")
st.dataframe(filtro, use_container_width=True)

# Botão para exportar CSV
st.download_button("Exportar dados filtrados", data=filtro.to_csv(index=False).encode('utf-8'),
                   file_name='redecris_mulher_filtrado.csv', mime='text/csv')
