#!/usr/bin/python
# -*- coding: latin-1 -*-

import streamlit as st
import numpy
import pandas as pd
import matplotlib.pyplot as plt

st.title('App da Aline')

states_available = ['SP']
cities_available = ['Santos']

state_option = st.selectbox(
     'Selecione o estado',
     states_available)

city_option = st.selectbox(
     'Selecione a cidade',
     cities_available)

FILEPATHS = { # For october only
    'comissionados_nao_quadro':'comissionados_nao_quadro_out.xls',
    'comissionados_quadro':'comissionados_quadro_out.xls',
    'folha_pgto':'folha_pgto_out.xls',
    'media_salario':'media_salario_out.xls',
    'servants': 'servidores_out.xls'
}
def get_filepath(key):
    return FILEPATHS[key]

my_placeholder = st.empty()

# reading files
servidores = pd.read_excel('../data/{}'.format(get_filepath('servants'))).dropna()
comissionados_nao_quadro = pd.read_excel('../data/{}'.format(get_filepath('comissionados_nao_quadro'))).dropna()
comissionados_quadro = pd.read_excel('../data/{}'.format(get_filepath('comissionados_quadro'))).dropna()

#st.table(comissionados_quadro[:5])

count_nao_quadro = len(comissionados_nao_quadro)
count_ = len(comissionados_nao_quadro)
kpi = (len(comissionados_nao_quadro) + len(comissionados_quadro))/(len(comissionados_quadro) + len(servidores))
#st.subheader('KPI1 : {:.2f}% of servants comissionados over all servants'.format(100.*kpi))

my_placeholder.text('{}/{} : {:.2f}% of servants comissionados over all servants'.format(city_option,state_option, 100*kpi))


# Breakdown by dept
#st.subheader('Breakdown by department (top 10)')
# lotacao = "Lota" u"\u00E7" + u"\u00E3" + "o"
# grouped = servidores[servidores['Tipo de Servidor']==servidores['Tipo de Servidor'].unique()[1]]\
# .groupby([lotacao], as_index=False)\
# .agg({'Registro':'count'}).sort_values(by='Registro',ascending=False)

# st.table(grouped[:10].reset_index(drop=True))
