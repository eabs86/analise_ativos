
"""
Created on Thu Mar  9 09:23:11 2023

@author: Emmanuel Andrade
"""
from datetime import datetime
import pandas as pd #carregando a biblioteca
import numpy as np
import matplotlib.pyplot as plt
from funcoes_auxiliares import object_to_float, normalizar_serie
from funcoes_auxiliares import retorno_e_stats, grafico_retornos_diarios,calculo_drawdown




""" 
1º Etapa: Carregamento dos dados e alteração do nome das colunas.

"""


btcusd = pd.read_csv("dataset/_BTCUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
btcusd.rename(columns={'Data':'date',
                       'Último':'close',
                       'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

dxy = pd.read_csv("dataset/_DXY.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
dxy.rename(columns={'Data':'date',
                    'Último':'close',
                    'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

ethusd = pd.read_csv("dataset/_ETHUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
ethusd.rename(columns={'Data':'date',
                       'Último':'close',
                       'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

ibovespa = pd.read_csv("dataset/_IBOVESPA.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
ibovespa.rename(columns={'Data':'date',
                         'Último':'close',
                         'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

nasdaq = pd.read_csv("dataset/_NASDAQ.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
nasdaq.rename(columns={'Data':'date',
                       'Último':'close',
                       'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

ouro = pd.read_csv("dataset/_OUROUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
ouro.rename(columns={'Data':'date',
                     'Último':'close',
                     'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)


sp500 = pd.read_csv("dataset/_SP500.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
sp500.rename(columns={'Data':'date',
                      'Último':'close',
                      'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

usdbrl = pd.read_csv("dataset/_USDBRL.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
usdbrl.rename(columns={'Data':'date',
                       'Último':'close',
                       'Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

""" 
2º Etapa: Convertendo a coluna de data para o formato datetime
"""

btcusd['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in btcusd['date']]
btcusd['date'] = pd.to_datetime(btcusd['date'], format='%d/%m/%Y')

dxy['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in dxy['date']]
dxy['date'] = pd.to_datetime(dxy['date'], format='%d/%m/%Y')

ethusd['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in ethusd['date']]
ethusd['date'] = pd.to_datetime(ethusd['date'], format='%d/%m/%Y')

ibovespa['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in ibovespa['date']]
ibovespa['date'] = pd.to_datetime(ibovespa['date'], format='%d/%m/%Y')

nasdaq['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in nasdaq['date']]
nasdaq['date'] = pd.to_datetime(nasdaq['date'], format='%d/%m/%Y')

ouro['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in ouro['date']]
ouro['date'] = pd.to_datetime(ouro['date'], format='%d/%m/%Y')

# prata['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in prata['date']]
# prata['date'] = pd.to_datetime(prata['date'], format='%d/%m/%Y')

usdbrl['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in usdbrl['date']]
usdbrl['date'] = pd.to_datetime(usdbrl['date'], format='%d/%m/%Y')

sp500['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in sp500['date']]
sp500['date'] = pd.to_datetime(sp500['date'], format='%d/%m/%Y')

""" 
3º Etapa: Análise individual de cada série

"""

ethusd = object_to_float(ethusd)
btcusd = object_to_float(btcusd)
ibovespa = object_to_float(ibovespa)
sp500 = object_to_float(sp500)
nasdaq = object_to_float(nasdaq)
# dxy = object_to_float(dxy) já está float na base de dados
dxy.set_index('date',inplace=True)
# usdbrl = object_to_float(usdbrl) já está float na base de dados
usdbrl.set_index('date',inplace=True)
ouro = object_to_float(ouro)



btcusd_new_dataframe = retorno_e_stats(btcusd).dropna(axis=0)

plt.figure()
grafico_retornos_diarios(btcusd_new_dataframe['returns']*100,"Retornos diários do BTC/USD")

retorno_acumulado_btc = (1+btcusd_new_dataframe['returns']).cumprod()
drawdown_btc, max_drawdown_btc = calculo_drawdown(btcusd_new_dataframe['returns'])


fig = plt.figure(figsize=(16,9))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,3)
ax1.plot(drawdown_btc['retornos_acumulados'])
ax2.plot(drawdown_btc['drawdown']*100, color='r')
ax1.set_ylabel('Retorno acumulado')
ax1.set_xlabel('Anos')
ax2.set_ylabel('Drawdown em %')
ax2.set_xlabel('Anos')


returns_percent = btcusd_new_dataframe['returns']*100
returns_percent.describe()

dados_btcusd_2015 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2015].reset_index(drop=True)
dados_btcusd_2016 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2016].reset_index(drop=True)
dados_btcusd_2017 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2017].reset_index(drop=True)
dados_btcusd_2018 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2018].reset_index(drop=True)
dados_btcusd_2019 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2019].reset_index(drop=True)
dados_btcusd_2020 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2020].reset_index(drop=True)
dados_btcusd_2021 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2021].reset_index(drop=True)
dados_btcusd_2022 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2022].reset_index(drop=True)
dados_btcusd_2023 = btcusd_new_dataframe.loc[btcusd_new_dataframe.index.year == 2023].reset_index(drop=True)

fechamento_por_ano = pd.concat(
    [dados_btcusd_2015['close'],
    dados_btcusd_2016['close'],
    dados_btcusd_2017['close'],
    dados_btcusd_2018['close'],
    dados_btcusd_2019['close'],
    dados_btcusd_2020['close'],
    dados_btcusd_2021['close'],
    dados_btcusd_2022['close'],
    dados_btcusd_2023['close']],
    keys=['btcusd_2015',
        'btcusd_2016',
        'btcusd_2017',
        'btcusd_2018',
        'btcusd_2019',
        'btcusd_2020',
        'btcusd_2021',
        'btcusd_2022',
        'btcusd_2023',],axis=1
)
plt.figure()

#plot dos gráficos ano por ano num único gráfico
ax3 = (normalizar_serie(fechamento_por_ano)).plot(title="Comportamento do BTC/USD em cada ano")
ax3.set_ylabel('Retorno Percentual %')
ax3.set_xlabel('Tempo (em dias)')
plt.show()

retorno_2015_acumulado=(1+dados_btcusd_2015['returns']).cumprod()-1
retorno_2015_log_acumulado = np.exp(dados_btcusd_2015['returns_log'].values.cumsum()) - 1

dataframe_drawdown_btc2015, max_drawdown_btc2015 = calculo_drawdown(dados_btcusd_2015['returns'])

describe_dados_btcusd_2015 = dados_btcusd_2015.describe()

retorno_medio_anual_btcusd2015 = describe_dados_btcusd_2015.iloc[1,4]*365
variancia_media__anual_btcusd2015 = dados_btcusd_2015['returns'].var()*365
desviopadrao_medio_anual_btcusd2015 = describe_dados_btcusd_2015.iloc[2,4]*(365**0.5)
open_to_close_media_btcusd2015 =  describe_dados_btcusd_2015.iloc[2,6]
min_to_max_media_btcusd2015 =  describe_dados_btcusd_2015.iloc[2,7]

#correlação entre ativos



