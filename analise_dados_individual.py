
"""
Created on Thu Mar  9 09:23:11 2023

@author: Emmanuel Andrade
"""
from datetime import datetime
import pandas as pd #carregando a biblioteca
import numpy as np
import matplotlib.pyplot as plt
from funcoes_auxiliares import object_to_float, normalizar_serie
from funcoes_auxiliares import retornos_e_stats, grafico_retornos_diarios,calculo_drawdown
from funcoes_auxiliares import grafico_retorno_drawdown,grafico_retorno_drawdown_multiplos




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


usdbrl['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in usdbrl['date']]
usdbrl['date'] = pd.to_datetime(usdbrl['date'], format='%d/%m/%Y')

sp500['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in sp500['date']]
sp500['date'] = pd.to_datetime(sp500['date'], format='%d/%m/%Y')

""" 
3º Etapa: Conversão dos dados para float.

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

""" 
4º Etapa: Inicio da análise dedados.
- Criação de um novo dataframe com algumas métricas como retorno simples, retorno log normal e outras.
Para saber mais, consultar funcoes_auxiliares.py

"""

btcusd_new_dataframe = retornos_e_stats(btcusd)


grafico_retornos_diarios(btcusd_new_dataframe['returns']*100,"Retornos diários do BTC/USD")


drawdown_btc, max_drawdown_btc = calculo_drawdown(btcusd_new_dataframe['returns'])


grafico_retorno_drawdown(drawdown_btc, 'Retorno Acumulado do BTC/USD x Drawdown no período')

sp500_new_dataframe = retornos_e_stats(sp500).dropna(axis=0)
drawdown_sp500, max_drawdown_sp500=calculo_drawdown(sp500_new_dataframe['returns'])
grafico_retorno_drawdown(drawdown_sp500,'')


ibovespa_new_dataframe = retornos_e_stats(ibovespa).dropna(axis=0)
drawdown_ibovespa, max_drawdown_ibovespa=calculo_drawdown(ibovespa_new_dataframe['returns'])
grafico_retorno_drawdown(drawdown_ibovespa,'Retorno do Ibovespa x Drawdown no período')

ouro_new_dataframe = retornos_e_stats(ouro).dropna(axis=0)
drawdown_ouro, max_drawdown_ouro=calculo_drawdown(ouro_new_dataframe['returns'])
grafico_retorno_drawdown(drawdown_ouro,'Retorno do ouro x Drawdown no período')

usdbrl_new_dataframe = retornos_e_stats(usdbrl).dropna(axis=0)
drawdown_usdbrl, max_drawdown_usdbrl=calculo_drawdown(usdbrl_new_dataframe['returns'])
grafico_retorno_drawdown(drawdown_usdbrl,'Retorno do usdbrl x Drawdown no período')

grafico_retorno_drawdown_multiplos([drawdown_ibovespa,drawdown_sp500,drawdown_ouro,drawdown_usdbrl],['Ibovespa', 'SP500','Ouro','USDBRL'])


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



