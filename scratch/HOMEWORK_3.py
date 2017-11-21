import pandas as pd
import numpy as np
import datetime
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu


order_file = 'orders.csv'
curr_cash = 10000

##C:/Users/Karim/Anaconda3/envs/py27/python.exe

## Process Orders File
orderFile = pd.read_csv(order_file, header=None)

# Get list of symbols
ls_symbols = list(np.unique(orderFile[[3]].values))


dfOrders = pd.DataFrame(columns=['OrderDateTime', 'SYM', 'ACTION', 'AMOUNT'])
for index, row in orderFile.iterrows():
    line = pd.Series({
        'OrderDateTime' : datetime.datetime(row[0],row[1], row[2], 16),
        'SYM' : row[3],
        'ACTION' : row[4],
        'AMOUNT' : row[5]
                     })

    dfOrders = dfOrders.append(line, ignore_index=True)

dfOrders = dfOrders.set_index('OrderDateTime')
dfOrders = dfOrders.sort_index()


# Get list of dates
dt_start = dfOrders.index.min()
dt_end = dfOrders.index.max()

##
# Get market data
dataobj = da.DataAccess('Yahoo')
ls_keys = ['close', 'actual_close']
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, datetime.timedelta(hours=16))


ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)

d_data = dict(zip(ls_keys, ldf_data))
ls_symbols.append("CASH")

dfTrades = pd.DataFrame(index=ldt_timestamps, columns=ls_symbols)

## Process

dfTrades["CASH"][ldt_timestamps[0]] = curr_cash

curr_stocks = dict()
for sym in ls_symbols:
    curr_stocks[sym] = 0
    dfTrades[sym][ldt_timestamps[0]] = 0


for index, row in dfOrders.iterrows():
    SYM = row['SYM']
    CURR_DATE = index
    PRICE = d_data['close'][SYM][CURR_DATE]

    AMOUNT = row['AMOUNT']
    ACTION = row['ACTION']

    if ACTION == 'buy':
        curr_cash = curr_cash - (AMOUNT * PRICE)
        dfTrades['CASH'][CURR_DATE] = curr_cash
        curr_stocks[sym] = curr_stocks[sym] + AMOUNT
        dfTrades[SYM][CURR_DATE] = curr_stocks[sym]
    else:
        curr_cash = curr_cash + (AMOUNT * PRICE)
        dfTrades['CASH'][CURR_DATE] = curr_cash
        curr_stocks[sym] = curr_stocks[sym] - AMOUNT
        dfTrades[SYM][CURR_DATE] = curr_stocks[sym]


dfTrades = dfTrades.fillna(method='pad')
print dfTrades
