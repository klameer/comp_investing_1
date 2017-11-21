import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da # Class to read data into QSTK

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
dt_start = dt.datetime(2011,1,1)
dt_end = dt.datetime(2011,12,31)
dt_timeofday = dt.timedelta(hours=16) # we need this to get data from the closing time
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))

na_price = d_data['close'].values
na_normalized = na_price / na_price[0,:]

fig = plt.figure()


ax1 = fig.add_subplot(2,2,1)
ax1.plot(ldt_timestamps, na_price)
ax1.set_title('Price Movement') # Not sure why this isn't working
ax1.legend(ls_symbols)
ax1.set_xlabel('Adjusted Close')
ax1.set_ylabel('Date')

ax2 = fig.add_subplot(2,2,2)
ax2.plot(ldt_timestamps, na_normalized)
ax2.set_title('Adjusted Price Movement')
ax2.legend(ls_symbols)
ax2.set_xlabel('Normalized Close')
ax2.set_ylabel('Date')

## Daily Returns
na_rets = na_normalized.copy()
na_rets = tsu.returnize0(na_rets)
ax3 = fig.add_subplot(2,2,3)
ax3.scatter(na_rets[:,3], na_rets[:,1], color='blue')
ax3.set_title('Correlation between GLD and $SPX')
ax3.set_xlabel('$SPX')
ax3.set_ylabel('GLD')

ax4 = fig.add_subplot(2,2,4)
ax4.scatter(na_rets[:,4], na_rets[:,3], color='orange')
p = np.polynomial.Polynomial.fit(na_rets[:,4], na_rets[:,3],4)
ax4.plot(*p.linspace())
ax3.set_title('Coorelation between $SPX and XOM')
ax3.set_xlabel('XOM')
ax3.set_ylabel('$SPX')
