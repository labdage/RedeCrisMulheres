
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='RedeCRIS Mulher', layout='wide')
st.title('RedeCRIS Mulher')
st.subheader('Conectando dados, pesquisas e políticas no enfrentamento à violência de gênero.')

df = pd.read_csv('base_geral.csv')

with st.sidebar:
    st.header('Filtros')
    grupo = st.selectbox('Grupo de Pesquisa', ['Todos'] + sorted(df['Grupo'].dropna().unique()))
    pesquisador = st.selectbox('Pesquisador(a)', ['Todos'] + sorted(df['Pesquisador'].dropna().unique()))
    instituicao = st.selectbox('Instituição', ['Todas'] + sorted(df['Instituicao'].dropna().unique()))
    tipo = st.selectbox('Tipo de Produção', ['Todos'] + sorted(df['Tipo'].dropna().unique()))
    tema = st.selectbox('Tema', ['Todos'] + sorted(df['Tema'].dropna().unique()))
    ano = st.selectbox('Ano', ['Todos'] + sorted(df['Ano'].dropna().astype(str).unique()))

filtered = df.copy()
if grupo != 'Todos':
    filtered = filtered[filtered['Grupo'] == grupo]
if pesquisador != 'Todos':
    filtered = filtered[filtered['Pesquisador'] == pesquisador]
if instituicao != 'Todas':
    filtered = filtered[filtered['Instituicao'] == instituicao]
if tipo != 'Todos':
    filtered = filtered[filtered['Tipo'] == tipo]
if tema != 'Todos':
    filtered = filtered[filtered['Tema'] == tema]
if ano != 'Todos':
    filtered = filtered[filtered['Ano'].astype(str) == ano]

st.dataframe(filtered)

st.subheader('Distribuição por UF')
if 'UF' in filtered.columns:
    mapa = filtered.groupby('UF').size().reset_index(name='Contagem')
    fig = px.choropleth(locations=mapa['UF'], locationmode='ISO-3166-2', color=mapa['Contagem'],
                        scope='south america', title='Produção por Estado')
    st.plotly_chart(fig, use_container_width=True)

st.download_button("Exportar dados filtrados", data=filtered.to_csv(index=False).encode('utf-8'),
                   file_name='redecris_mulher_filtrado.csv', mime='text/csv')
