# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:38:45 2017

@author: Karim
Analyze portfolio created from mktsim
"""

import pandas as pd
import numpy as np
import datetime 
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da 
import QSTK.qstkutil.tsutil as tsu

NUM_TRADING_DAYS = 252

ls_symbols = ['$SPX']

value_file = 'values.csv'

dfValues = pd.read_csv(value_file, header=None)


portVal = dfValues[dfValues.columns[3]].values.copy()
portVal = portVal.astype('float')
portVal = portVal / portVal[0]
dailyVal = portVal.copy()
tsu.returnize0(dailyVal)

daily_ret = np.mean(dailyVal)
vol = np.std(dailyVal)
sharpe = np.sqrt(NUM_TRADING_DAYS) * daily_ret / vol
cum_ret = portVal[len(portVal) -1]/portVal[0]

print "=== FUND ==="
print "Sharpe Ratio: ", sharpe
print "Volatility (stdev): ", vol
print "Average Daily Return: ", daily_ret
print "Cumulative Return: ", cum_ret

## Get benchmark data
intLastLine = len(dfValues) - 1
dt_start = datetime.datetime(dfValues[0][0], dfValues[1][0], dfValues[2][0])
dt_end = datetime.datetime(dfValues[0][intLastLine], dfValues[1][intLastLine], dfValues[2][intLastLine])

# Getting market data
dataobj = da.DataAccess('Yahoo')
ls_keys = ['close', 'actual_close']
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, datetime.timedelta(hours=16))

ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))

temp = d_data['close'].values.copy()
portVal = temp / temp[0,:]

dailyVal = portVal.copy()
tsu.returnize0(dailyVal)

# Calculate statistics
daily_ret = np.mean(dailyVal)
vol = np.std(dailyVal)
sharpe = np.sqrt(NUM_TRADING_DAYS) * daily_ret / vol
cum_ret = float(portVal[len(portVal) -1]/portVal[0])

print "=== BENCH ==="
print "Sharpe Ratio: ", sharpe
print "Volatility (stdev): ", vol
print "Average Daily Return: ", daily_ret
print "Cumulative Return: ", cum_ret
