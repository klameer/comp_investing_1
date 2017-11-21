# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:54:20 2017

@author: Karim
Computational Investing Quiz 6
Implement Bollinger Bands
"""

import pandas as pd
import pandas_datareader.data as web
import datetime as dt 


def bollinger(sym, dt_start, dt_end):
    
    df = web.DataReader(sym, 'yahoo', dt_start, dt_end)
    
    df_close = df['Close']
    df_mean = pd.rolling_mean(df_close, 20)
    df_std = pd.rolling_std(df_close, 20)
    df_bands = (df_close - df_mean) / df_std
    
    return df_bands

if __name__ == '__main__':
    dt_start = dt.datetime(2010,1,1, 16)
    dt_end = dt.datetime(2010,12,31, 16)
    
    dt_find = dt.datetime(2010, 6, 23)
    sym = 'MSFT'
    
    sBands = bollinger(sym, dt_start, dt_end)
    print sBands[dt_find]
    