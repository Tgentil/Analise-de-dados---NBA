import streamlit as st
import pandas as pd

# Carregar dados
data = pd.read_csv('./out/player_totals_updated.csv')

# Criando o dashboard
st.title('Dashboard de Estatísticas da NBA')
st.write("Exploração Interativa das Estatísticas dos Jogadores da NBA")

# Adicionar filtros de posição e ano
year = st.selectbox('Escolha um ano para visualizar estatísticas', data['season'].unique())
position = st.selectbox('Escolha uma posição para visualizar estatísticas', data['pos'].unique())

# Filtrar dados com base nos filtros selecionados
filtered_data = data[(data['season'] == year) & (data['pos'] == position)]

# Exibir estatísticas filtradas
st.write(filtered_data[['player', 'pts', 'ast', 'trb', 'blk']])

# Carregar dados de estatísticas por posição
stats_by_position = pd.read_csv('./out/stats_by_position_year.csv')

# Filtrar dados de estatísticas por posição e ano
filtered_stats_by_position = stats_by_position[(stats_by_position['season'] == year) & (stats_by_position['pos'] == position)]

# Exibir estatísticas médias por posição e ano
st.write(f"Estatísticas Médias para a Posição {position} no Ano {year}:")
st.write(filtered_stats_by_position)
