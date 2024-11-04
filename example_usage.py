from Financiers.stock import Stock

stock = Stock()
print(stock.company_overview("IBM"))


info = stock.Stockprice_getter("AAPL")
print(info)

sma = stock.calculate_sma(info, window=20)
ema = stock.calculate_ema(info, span=20)
print(sma)
print(ema)

print(stock.detect_crossover(sma, ema))
print(stock.calculate_rolling_std(info, window=20))
print(stock.calculate_daily_returns(info))
print(stock.calculate_atr(info,window=14))
print(stock.calculate_true_range(info))
print(stock.calculate_momentum(info, period=10))
print(stock.calculate_roc(info, period=10))
print(stock.calculate_volume_moving_average(info, window=20))
print(stock.calculate_vpt(info))
print(stock.calculate_bollinger_bands(info, window=20, num_std_dev=2))
print(stock.calculate_rsi(info, period=14))
print(stock.calculate_stochastic_oscillator(info, period=14))
print(stock.calculate_daily_range(info))
print(stock.detect_doji(info, tolerance=0.001))
print(stock.detect_engulfing(info))
print(stock.calculate_cumulative_return(info))
print(stock.calculate_sharpe_ratio(info, risk_free_rate=0.01, period=252))
print(stock.calculate_daily_returns(info))