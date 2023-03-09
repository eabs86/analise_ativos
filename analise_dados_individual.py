# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:23:11 2023

@author: Emmanuel Andrade
"""

import pandas as pd #carregando a biblioteca
import numpy as np
from datetime import datetime


def object_to_float(dataframe_object):
    coluna_datas = dataframe_object['date'].copy()
    dataframe_object.drop('date',axis="columns",inplace=True)
    dataframe_object = dataframe_object.stack().str.replace('.','').unstack()
    dataframe_object = dataframe_object.stack().str.replace(',','.').unstack()
    dataframe_float = dataframe_object.astype(float)
    dataframe_float['date']=coluna_datas
    dataframe_float.set_index('date',inplace=True)
    
    return dataframe_float

def retorno_e_stats(dataframe):
    
    
    return new_dataframe

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
3º Etapa: Análise individual de cada série

"""

ethusd = object_to_float(ethusd)
btcusd = object_to_float(btcusd)
ibovespa = object_to_float(ibovespa)
sp500 = object_to_float(sp500)
nasdaq = object_to_float(nasdaq)
dxy = object_to_float(dxy)
usdbrl = object_to_float(usdbrl)
ouro = object_to_float(ouro)
prata = object_to_float(prata)


