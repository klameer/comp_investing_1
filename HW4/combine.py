# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:32:01 2017

@author: Karim
"""

import QSTK.qstkutil.qsdateutil as du
import datetime
from event import create_orders
from mktsim import simulate
from analyze import analyze

order_file = 'orders.csv'
value_file = 'values.csv'

eventAmount = 10.00
dt_start = datetime.datetime(2008,1,1)
dt_end = datetime.datetime(2009,12,31)
strSymbols = 'sp5002012'
curr_cash = 50000


ldt_timestamps = du.getNYSEdays(dt_start, dt_end, datetime.timedelta(hours=16))
## Create the orders file
create_orders(ldt_timestamps, strSymbols, eventAmount) 
simulate(order_file, value_file, curr_cash)
analyze(value_file)
