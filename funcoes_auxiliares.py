import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def object_to_float(dataframe_object):
    coluna_datas = dataframe_object['date'].copy()
    dataframe_object.drop('date',axis="columns",inplace=True)
    dataframe_object = dataframe_object.stack().str.replace('.','').unstack()
    dataframe_object = dataframe_object.stack().str.replace(',','.').unstack()
    dataframe_float = dataframe_object.astype(float)
    dataframe_float['date']=coluna_datas
    dataframe_float.set_index('date',inplace=True)
    
    return dataframe_float

def normalizar_serie(serie):
    serie_normalizada = ((serie/serie.iloc[0])-1)*100
    
    return serie_normalizada

def retorno_e_stats(dataframe):
    
    dataframe['returns'] = (dataframe['close']/dataframe['close'].shift(1))-1
    dataframe['open_to_close_amplitude'] = np.abs(dataframe['open'] - dataframe['close'])
    dataframe['min_to_max_amplitude'] = np.abs(dataframe['min'] - dataframe['max'])
    new_dataframe = dataframe
    
    return new_dataframe

def grafico_retornos_diarios(dataframe):

    ax = dataframe.plot(label ='Retornos', alpha=0.6,
                                                    title='Retornos diários do BTC/USD em %')

    ax.set_ylabel('Retorno diários percentual %')
    ax.set_xlabel('Tempo')
    ax.axhline(dataframe.mean(), label='Média', color='k',linestyle='--')
    ax.axhline(dataframe.std()*2, label='2 desvios', color='orange',linestyle='--')
    ax.axhline(dataframe.std()*-2, color='orange',linestyle='--')
    ax.axhline(dataframe.std()*3, label='3 desvios', color='red',linestyle='--')
    ax.axhline(dataframe.std()*-3, color='red',linestyle='--')
    ax.legend(loc='best')
    
    return ax
    
