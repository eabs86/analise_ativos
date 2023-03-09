# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:23:11 2023

@author: Emmanuel Andrade
"""

import pandas as pd #carregando a biblioteca
import numpy as np
from datetime import datetime


def object_to_float(dataframe_object):
    dataframe_object.drop('date',axis="columns",inplace=True)
    dataframe_object = dataframe_object.stack().str.replace('.','').unstack()
    dataframe_object = dataframe_object.stack().str.replace(',','.').unstack()
    dataframe_float = dataframe_object.astype(float)
    
    return dataframe_float

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

prata = pd.read_csv("dataset/_PRATAUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
prata.rename(columns={'Data':'date','Último':'close','Abertura':'open','Máxima':'max','Mínima':'min'}, inplace=True)

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

prata['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in prata['date']]
prata['date'] = pd.to_datetime(prata['date'], format='%d/%m/%Y')

usdbrl['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in usdbrl['date']]
usdbrl['date'] = pd.to_datetime(usdbrl['date'], format='%d/%m/%Y')

sp500['date'] = [datetime.strptime(elemento, "%d.%m.%Y") for elemento in sp500['date']]
sp500['date'] = pd.to_datetime(sp500['date'], format='%d/%m/%Y')

""" 
3º Etapa: usando a série mais jovem como referência, que é a série da prata

"""
tamanho_serie_jovem = len(prata)

btcusd = btcusd.iloc[len(btcusd) - tamanho_serie_jovem:,:].reset_index(drop=True)
ethusd = ethusd.iloc[len(ethusd) - tamanho_serie_jovem:,:].reset_index(drop=True)
ibovespa = ibovespa.iloc[len(ibovespa) - tamanho_serie_jovem:,:].reset_index(drop=True)
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
prata = prata.loc[prata['date'].isin(sp500['date'])]

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
prata = prata.iloc[len(prata) - tamanho_serie_jovem:,:].reset_index(drop=True)

""" 
6º Etapa: Transformando os dados em float

"""

coluna_datas = ethusd['date'].copy()

ethusd = object_to_float(ethusd)
ethusd['date']=coluna_datas
ethusd.set_index('date',inplace=True)
