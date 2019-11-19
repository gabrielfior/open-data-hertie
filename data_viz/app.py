#!/usr/bin/python
# -*- coding: latin-1 -*-

import streamlit as st
import numpy
import pandas as pd
import matplotlib.pyplot as plt

st.title('My first app')
st.write('Write1','line2')

FILEPATHS = { # For october only
    'comissionados_nao_quadro':'comissionados_nao_quadro_out.xls',
    'comissionados_quadro':'comissionados_quadro_out.xls',
    'folha_pgto':'folha_pgto_out.xls',
    'media_salario':'media_salario_out.xls',
    'servants': 'servidores_out.xls'
}
def get_filepath(key):
    return FILEPATHS[key]

# reading files
servidores = pd.read_excel('../data/{}'.format(get_filepath('servants'))).dropna()
comissionados_nao_quadro = pd.read_excel('../data/{}'.format(get_filepath('comissionados_nao_quadro'))).dropna()
comissionados_quadro = pd.read_excel('../data/{}'.format(get_filepath('comissionados_quadro'))).dropna()

st.table(comissionados_quadro[:5])

nao_quadro_percentage = len(servidores[servidores['Tipo de Servidor']==servidores['Tipo de Servidor'].unique()[1]])/len(servidores)
st.subheader('KPI1 : {:.2f}% of servants comissionados over all servantes'.format(100.*nao_quadro_percentage))

st.subheader('Breakdown by department (top 10)')

# Breakdown by dept
lotacao = "Lota" u"\u00E7" + u"\u00E3" + "o"
grouped = servidores[servidores['Tipo de Servidor']==servidores['Tipo de Servidor'].unique()[1]]\
.groupby([lotacao], as_index=False)\
.agg({'Registro':'count'}).sort_values(by='Registro',ascending=False)

st.table(grouped[:10].reset_index(drop=True))
