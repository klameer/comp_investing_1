I am able to learn anything if I set my mind to it.

## Module 8
Jensen's Alpha
The CAPM asserts that alpha must be zero if the return on the asset or portfolio represents the beta of the asset.
Alpha is then a measure of the portfolio managers skill.
An alpha of zero means that any payments to a portfolio manager is not worth it because you might as well invest that in the market.

Back testing - The process of testing a trading system on prior periods
Run a simulation of your strategy on prior periods to test the feasibility of the strategy.


## Module 7
Information feeds
Reuters machine readable news
StarMine
InsiderInsights


## Module 6
Data
Survivor bias - When you are comparing a portfolio with what was there historically, you only see the companies that have survived. The data about the companies that died will not be in your analysis because they don't exist anymore.
You need to make your analysis survivor bias free. This could be by taking many random portfolios and testing the trading strategy on all of them.

Actual Price - Value posted on the exchange at a specific time in history
Adjusted price - Revised price that automatically accounts for how much you would have made if you held the stock. Adjust for splits and dividends. Adjusted price is calculated by changing the history of the stock to a standard.

For NaNs you can fill back or fill forward. When you are filling, always fill forward first and then fill back. This removes Nans before the stock started trading.

Sanity Checks on Data
Scan for 50% drops or 200% gains
NaNs on DOW stocks
Recent adjusted prices less than $0.01
NaNs > 20 trading days

Good data is important
If you data isn't good you may discover false patterns in your data


## Module 5
Event Studies and the Efficient Market Hypotheses
Arbitrage could mean what the price of an equity is on the market and what we believe its true value is.

Two general approaches to determining value.
Technical Analysis - Price and volume only
Fundamental Analysis - Financial statements and metrics

Where does the information come from
Price/Volume : The market
Fundamentals : SEC Filings
News : Exogenous Sources

Efficient Market Hypothesis
Weak: Prices reflect all past and publicly available information. Prohibits profit from technical analysis. Fundamental information that hasn't yet been revealed and is taking some time to percolate in the news can be exploited.
Semi Strong: Weak + Prices change instantly to reflect new publicly available information. Prohibits profit from technical analysis and fundamental analysis.
Strong: Semi Strong + Prices react immediately. This includes insider trading. Hidden Information.


# Metrics
These are what will be used in the website
Annual Return - (Value End / Value Start) - 1
Risk - Standard Deviation of daily returns
Sharpe Ratio - The higher the Sharpe Ratio the better. Reward over risk
    k* (mean(daily returns) / stdev(daily_rets))
    k = sqrt(250) for daily returns

Common Metrics
Annual Return
Risk: Standard Deviation of Return
Risk Drawdown: How much the portfolio goes down when the market goes down
Risk/Reward: Sharpe Ratio: How much reward you're getting for how much risk you're taking
Risk/Reward: Sortino Ratio: Counts volatility up



## Learning Objectives
1. Become familiar with electronic markets
2. Interpret Market Data
3. Write software to visualize market data
4. Create a market simulator



Market Order - Buy or Sell at whatever the price. A market order buys shares at the lowest available price.
Limit Order - Set a max for buy or a min for sell
Ask Price - What people are willing to buy their shares for
Bid Price - How much people are willing to sell their shares for

Spread - The difference between the lowest someone is willing to sell their shares for and the highest someone is willing to buy shares for. Spread represents limit orders.
Crossing the spread is when someone raises the price they want to buy and buys shares at the lowest sell price.
High frequency trading. Looks at the order book and sees if there are more people buying or selling and predicts marked movement based on this.
Brokers facilitate short selling

## MODULE 4 - What is the value of a company
Market Cap  - # Of Shares * Price per share
Future Dividends - dividend/(1-gamma) gamma being the discount rate
Book Value - If we split the company up, what is the sum of its parts

Fundamental Analysis - If you think a company is more valuable than its current stock price then this is an opportunity. Value is the sum of book value and the present values of future returns (intrinsic value).

Capital Assets Pricing Model (CAPM)
Assumptions
 - Return on stocks has two components
    - Systematic
    - Residual


## QSTK
```
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

ls_symbols = ["APPL", "GOOG", "$SPX", "XOM"]
dt_start = dt.datetime(2010,1,1)
dt_end = db.datetime(2010,1,15)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEDays(dt_start, dt_end, dt_timeofday)
c_dataobj = da.DataAccess("Yahoo")
ls_keys = ["open", "high", "low", "volume", "actual_close"]

d_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))
d_data["close"]
na_price = d_data["close"].values

# Create a Plot
plt.clf()
plt.plot(ldt_timestamps, na_price)
plt.legend(ls_symbols)
plt.xlabel("Date")
plt.ylabel("Adjusted Close")

# Normalize a prices for better comparison
na_price
na_normalized_price = na_price / na_price[0, : ] # divide by all columns in the first row


```


## Resources
wiki.quantsoftware.com
Active Portfolio Management
Hedge Funds

## Glossary
Alpha - The measure of active return on investment. The performance of that investment against a suitable market index. An alpha of 1% means that the investment was 1% better than the market during the period of time in question.
Active return - refers to a the segment of the investment portfolio return that is due to actively managing it rather than normal market movements. It is normally measured compared to a benchmark which could be an index return.
R2 - R Squared (Coefficient of determination) - What proportion of the dependent variable is predicted by the independent variable.
Sharpe Ratio - How well the return of the asset compensates the investor for the risk taken.
Jensen's Alpha - The abnormal return of a security of a security or a portfolio of securities over the theoretical expected return.
CAPM - Used to determine a theoretically appropriate required rate of return of an asset, to make a decision about adding assets to a well diversified portfolio.
Risk - The chance that an investments risk is not what is expected. Risk is usually measured by the standard deviation of prior returns. Or the average return on a specific investment.
Active risk - refers to a segment of an investment portfolio risk that is due to actively managing the portfolio rather than normal market movements. Like active return it is measured against a benchmark. It measures how well the portfolio follows the benchmark against which it is measured.
Information Ratio - Is the measure of risk adjusted return of a portfolio. It is defined as active return divided by active risk or tracking error.
Information Coefficient - Measures the predictive skill of the financial analysis. It is like correlation and measures what the analyst predicted against what actually happened.  
Beta - The assets movement relative to the market (i.e and index S&P 500). For example if an assets beta is 1.5, it will move 1.5 times the way the market moves. Therefore the market portfolio has a beta of 1 and risk free returns have a beta of 0. Beta allows us to separate excess returns into 2 components. The market element and residual element.

Residual Return/Risk - Risk/Return independent of a benchmark.
Excess Returns are total returns less risk free returns.

S&P 500 500 of the largest stocks in the US.
