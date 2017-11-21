# Import QSTK
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Import third party librararies
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt



#ls_allocations = [0.0, 0.0, 0.0, 1.0]


def simulate(dt_start, dt_end, ls_symbols, ls_allocations):
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    c_dataobj = da.DataAccess('Yahoo')

    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)

    d_data = dict(zip(ls_keys, ldf_data))

    df_close = d_data['close'].copy()

    arr_close = d_data["close"].values.copy()
    arr_norm_close = arr_close / arr_close[0,:]
    arr_alloc = np.array(ls_allocations).reshape(4,1)

    arr_portfolio = np.dot(arr_norm_close, arr_alloc)
    arr_portfolio = np.array(arr_norm_close * ls_allocations).sum(axis=1)

    ## Daily Returns
    arr_daily_returns = arr_portfolio.copy()
    arr_daily_returns = tsu.returnize0(arr_daily_returns)

    # Other Statistics
    vol = np.std(arr_daily_returns)
    daily_ret = np.mean(arr_daily_returns)
    sharpe = np.sqrt(TRADING_DAYS) * daily_ret / vol
    cum_ret = arr_portfolio[len(arr_portfolio) - 1]

    return vol, daily_ret, sharpe, cum_ret

# Get best allocation
#lst_allocations = []
def best_allocation(dt_start, dt_end, ls_symbols):
    max_sharpe = -1
    max_alloc = [0,0,0,0]
    #dt_start = dt.datetime(2010,1,1)
    #dt_end = dt.datetime(2010,12,31)
    #ls_symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']
    for i in np.arange(0.0, 1.1, 0.1):
        for j in np.arange(0.0, 1.1, 0.1):
            for k in np.arange(0.0, 1.1, 0.1):
                for l in np.arange(0.0, 1.1, 0.1):
                    if np.sum([i,j,k,l]) == 1:
                        ls_allocations = [i,j,k,l]
                        vol, daily_ret, sharpe, cum_ret = simulate(dt_start, dt_end, ls_symbols, ls_allocations)
                        #lst_allocations.append([i,j,k,l])
                        if sharpe > max_sharpe:
                            max_sharpe = sharpe
                            max_alloc = ls_allocations
    return max_alloc

TRADING_DAYS = 252

dt_start = dt.datetime(2010,1,1)
dt_end = dt.datetime(2010,12,31)
ls_symbols = ['C', 'GS', 'IBM', 'HNZ']

ls_allocation = best_allocation(dt_start, dt_end, ls_symbols)
print "optimum allocation %s" % ls_allocation

vol, daily_ret, sharpe, cum_ret = simulate(dt_start, dt_end, ls_symbols, ls_allocation)
print """
    stdev: %s
    daily_ret: %s
    sharpe: %s
    cum_ret: %s
""" % (vol, daily_ret, sharpe, cum_ret)
