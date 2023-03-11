import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def object_to_float(dataframe_object):
    '''
    
    Parameters
    ----------
    dataframe_object : dataframe
        É um dataframe que deve conter uma coluna nomeada de 'date'.

    Returns
    -------
    dataframe_float.

    '''    
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

def retornos_e_stats(dataframe):
    
    dataframe['returns'] = (dataframe['close']/dataframe['close'].shift(1))-1
    dataframe['cumulative_simple_return'] = (1+dataframe['returns']).cumprod()-1
    dataframe['returns_log'] = np.log((dataframe['close']/dataframe['close'].shift(1)))
    dataframe['cumulative_log_return']=np.exp(dataframe['returns_log'].cumsum()) - 1
    dataframe['open_to_close_amplitude'] = np.abs(dataframe['open'] - dataframe['close'])
    dataframe['min_to_max_amplitude'] = np.abs(dataframe['min'] - dataframe['max'])
    dataframe['otc_mintmax_ratio'] = dataframe['open_to_close_amplitude'] /  dataframe['min_to_max_amplitude']
    new_dataframe = dataframe.dropna(axis=0)
    
    return new_dataframe

def grafico_retornos_diarios(dataframe,titulo):

    ax = dataframe.plot(label ='Retornos', alpha=0.6,
                                                    title=titulo)

    ax.set_ylabel('Retorno diários em percentual %')
    ax.set_xlabel('Tempo em Anos')
    ax.axhline(dataframe.mean(), label='Média', color='k',linestyle='--')
    ax.axhline(dataframe.std()*2 + dataframe.mean() , label='2 desvios', color='orange',linestyle='--')
    ax.axhline(dataframe.std()*-2 + dataframe.mean(), color='orange',linestyle='--')
    ax.axhline(dataframe.std()*3 + dataframe.mean(), label='3 desvios', color='red',linestyle='--')
    ax.axhline(dataframe.std()*-3 + dataframe.mean(), color='red',linestyle='--')
    ax.legend(loc='best')
    
    return ax
    

def calculo_drawdown(retornos):
    retornos_acumulados = (1+retornos).cumprod()
    picos = retornos_acumulados.cummax()
    drawdown = (retornos_acumulados-picos)/picos
    max_drawdown = drawdown.min()*-100
    dataframe_saida = pd.DataFrame()
    dataframe_saida['retornos_acumulados'] = retornos_acumulados
    dataframe_saida['picos'] = picos
    dataframe_saida['drawdown'] = drawdown
    
    return dataframe_saida, max_drawdown

def grafico_retorno_drawdown(dataframe,titulo):
    
    fig = plt.figure(figsize=(16,9))
    fig.suptitle(titulo,fontsize=16)
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    ax1.plot(dataframe['retornos_acumulados'])
    ax2.plot(dataframe['drawdown']*100, color='r')
    ax1.set_ylabel('Retorno acumulado',fontsize=16)
    ax1.set_xlabel('Anos',fontsize=16)
    ax2.set_ylabel('Drawdown em %',fontsize=16)
    ax2.set_xlabel('Anos',fontsize=16)
    
def grafico_retorno_drawdown_multiplos(lista_dataframes):
    
    fig = plt.figure(figsize=(16,9))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    for dataframe in lista_dataframes:
    
        # fig.suptitle(titulo,fontsize=16)

        ax1.plot(dataframe['retornos_acumulados'])
        ax2.plot(dataframe['drawdown']*100)
        ax1.set_ylabel('Retorno acumulado',fontsize=16)
        ax1.set_xlabel('Anos',fontsize=16)
        ax2.set_ylabel('Drawdown em %',fontsize=16)
        ax2.set_xlabel('Anos',fontsize=16)
    

