# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:23:11 2023

@author: Emmanuel Andrade
"""

from datetime import datetime
import pandas as pd #carregando a biblioteca
import matplotlib.pyplot as plt
import seaborn as sns
from funcoes_auxiliares import object_to_float, normalizar_serie
from funcoes_auxiliares import retorno_e_stats, grafico_retornos_diarios


""" 
1º Etapa: Carregamento dos dados e alteração do nome das colunas.

"""


btcusd = pd.read_csv("dataset/_BTCUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
btcusd.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

dxy = pd.read_csv("dataset/_DXY.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
dxy.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

ethusd = pd.read_csv("dataset/_ETHUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
ethusd.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

ibovespa = pd.read_csv("dataset/_IBOVESPA.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
ibovespa.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

nasdaq = pd.read_csv("dataset/_NASDAQ.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
nasdaq.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

ouro = pd.read_csv("dataset/_OUROUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
ouro.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)


sp500 = pd.read_csv("dataset/_SP500.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
sp500.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

usdbrl = pd.read_csv("dataset/_USDBRL.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
usdbrl.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

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


df1 = object_to_float(btcusd)
df2 = object_to_float(ethusd)
btc_close = retorno_e_stats(df1)['returns']
eth_close = retorno_e_stats(df2)['returns']
df = pd.concat([btc_close,eth_close],keys=['returns_btc','returns_eth'], axis=1)

correl = df.corr()

""" 
3º Etapa: usando a série mais jovem como referência, que é a série da prata

"""
tamanho_serie_jovem = len(ibovespa)

btcusd = btcusd.iloc[len(btcusd) - tamanho_serie_jovem:,:].reset_index(drop=True)
ethusd = ethusd.iloc[len(ethusd) - tamanho_serie_jovem:,:].reset_index(drop=True)
sp500 = sp500.iloc[len(sp500) - tamanho_serie_jovem:,:].reset_index(drop=True)
nasdaq = nasdaq.iloc[len(nasdaq) - tamanho_serie_jovem:,:].reset_index(drop=True)
usdbrl = usdbrl.iloc[len(usdbrl) - tamanho_serie_jovem:,:].reset_index(drop=True)
dxy = dxy.iloc[len(dxy) - tamanho_serie_jovem:,:].reset_index(drop=True)
ouro = ouro.iloc[len(ouro) - tamanho_serie_jovem:,:].reset_index(drop=True)

""" 
4º Etapa: Alinhando as datas nas séries. Referência será sp500

"""

btcusd = btcusd.loc[btcusd['date'].isin(sp500['date'])]
ethusd = ethusd.loc[ethusd['date'].isin(sp500['date'])]
ibovespa = ibovespa.loc[ibovespa['date'].isin(sp500['date'])]
nasdaq = nasdaq.loc[nasdaq['date'].isin(sp500['date'])]
dxy = dxy.loc[dxy['date'].isin(sp500['date'])]
usdbrl = usdbrl.loc[usdbrl['date'].isin(sp500['date'])]
ouro = ouro.loc[ouro['date'].isin(sp500['date'])]


""" 
5º Etapa: Usando a menor série como referência (BTC ou ETH)

"""

tamanho_serie_jovem = len(btcusd)


ethusd = ethusd.iloc[len(ethusd) - tamanho_serie_jovem:,:].reset_index(drop=True)
ibovespa = ibovespa.iloc[len(ibovespa) - tamanho_serie_jovem:,:].reset_index(drop=True)
sp500 = sp500.iloc[len(sp500) - tamanho_serie_jovem:,:].reset_index(drop=True)
nasdaq = nasdaq.iloc[len(nasdaq) - tamanho_serie_jovem:,:].reset_index(drop=True)
usdbrl = usdbrl.iloc[len(usdbrl) - tamanho_serie_jovem:,:].reset_index(drop=True)
dxy = dxy.iloc[len(dxy) - tamanho_serie_jovem:,:].reset_index(drop=True)
ouro = ouro.iloc[len(ouro) - tamanho_serie_jovem:,:].reset_index(drop=True)
# prata = prata.iloc[len(prata) - tamanho_serie_jovem:,:].reset_index(drop=True)

""" 
6º Etapa: Transformando os dados em float

"""

# coluna_datas = ethusd['date'].copy()

ethusd = object_to_float(ethusd)
ethusd.reset_index(drop=True,inplace=True)
btcusd = object_to_float(btcusd)
btcusd.reset_index(drop=True,inplace=True)
sp500 = object_to_float(sp500)
sp500.reset_index(drop=True,inplace=True)
ibovespa = object_to_float(ibovespa)
ibovespa.reset_index(drop=True,inplace=True)
nasdaq = object_to_float(nasdaq)
nasdaq.reset_index(drop=True,inplace=True)
usdbrl.set_index('date',inplace=True)
usdbrl.reset_index(drop=True,inplace=True)
dxy.set_index('date',inplace=True)
dxy.reset_index(drop=True,inplace=True)
ouro = object_to_float(ouro)
ouro.reset_index(drop=True,inplace=True)



assets_retornos = pd.concat(
    [retorno_e_stats(ethusd)['returns'],
    retorno_e_stats(btcusd)['returns'],
    retorno_e_stats(sp500)['returns'],
    retorno_e_stats(nasdaq)['returns'],
    retorno_e_stats(ibovespa)['returns'],
    retorno_e_stats(dxy)['returns'],
    retorno_e_stats(usdbrl)['returns'],
    retorno_e_stats(ouro)['returns']],
    axis=1,
    keys=['ethusd','btcusd','sp500','nasdaq','ibovespa','dxy','usdbrl','ouro']
)



# assets_close.plot()
# plt.show()

#correlação entre as séries

correlacao_ativos = assets_retornos.dropna().corr()

sns.heatmap(correlacao_ativos,annot=True)
plt.show()

# normalização das séries

ethusd_norm_close = normalizar_serie(ethusd['close'])
btcusd_norm_close = normalizar_serie(btcusd['close'])
ibovespa_norm_close = normalizar_serie(ibovespa['close'])
sp500_norm_close = normalizar_serie(sp500['close'])
nasdaq_norm_close = normalizar_serie(nasdaq['close'])
dxy_norm_close = normalizar_serie(dxy['close'])
usdbrl_norm_close = normalizar_serie(usdbrl['close'])
# prata_norm_close = normalizar_serie(prata['close'])
ouro_norm_close = normalizar_serie(ouro['close'])

assets_close_norm = pd.concat(
    [ethusd_norm_close,
    btcusd_norm_close,
    sp500_norm_close,
    nasdaq_norm_close,
    ibovespa_norm_close,
    dxy_norm_close,
    usdbrl_norm_close,
    ouro_norm_close],
    axis=1,
    keys=['ethusd','btcusd','sp500','nasdaq','ibovespa','dxy','usdbrl','ouro']
)

ax1 = assets_close_norm[['ethusd','btcusd']].plot()
ax1.set_ylabel('Retorno Percentual %')
ax1.set_xlabel('Tempo')

ax2 = assets_close_norm[['nasdaq','ibovespa','dxy','usdbrl','ouro']].plot()
ax2.set_ylabel('Retorno Percentual %')
ax2.set_xlabel('Tempo')