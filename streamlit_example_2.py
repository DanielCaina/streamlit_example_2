import pandas as pd
import streamlit as st

df = pd.read_csv('covid-variants.csv')
pais = list(df['location'].unique())
variante = list(df['variant'].unique())

df['date'] = pd.to_datetime(df['date'], format='%y-%m-%d')

st.sidebar.selectbox('Escolha o pais', ['Todos'] + pais)
st.sidebar.selectbox('Escolha a variante', ['Todos'] + variante)

if(pais != 'Todos'):
    st.text('Mostrando resultado de ' + pais)
    df = df[df['location']== pais]

if(variante != 'Todos'):
    st.text('Mostrando resultado para variante ' + variante)
    df = df[df['variant']== variante]

dfShow = df.groupby(by = ['date']).sum() #soma os casos

import plotly.express as px

fig = px.line(dfShow, x=dfShow.index, y='num_sequences') #cria um grafico
fig.update_layout(title='casos diários de covid-19') #titulo do grafico
st.plotly_chart(fig, us_container_width=true) #manda o streamlit mostrar a figura