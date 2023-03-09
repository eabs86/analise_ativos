# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:23:11 2023

@author: apoco
"""
import pandas as pd
import numpy as np

btcusd = pd.read_csv("dataset\BTCUSD.csv",sep=',',decimal=',').drop(['Vol.','Var%'],axis=1)
