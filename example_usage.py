from Financiers.stock import Stock
from Financiers.stock import Company

stock = Stock()
print(stock.company_overview("IBM"))

company = Company()
info = company.Stockprice_getter("AAPL")
print(info)

sma = company.calculate_sma(info, window=20)
ema = company.calculate_ema(info, span=20)
print(sma)
print(ema)

print(company.detect_crossover(sma, ema))
print(company.calculate_rolling_std(info, window=20))
print(company.calculate_daily_returns(info))
print(company.calculate_atr(info,window=14))
print(company.calculate_true_range(info))
print(company.calculate_momentum(info, period=10))
print(company.calculate_roc(info, period=10))
print(company.calculate_volume_moving_average(info, window=20))
print(company.calculate_vpt(info))
print(company.calculate_bollinger_bands(info, window=20, num_std_dev=2))
print(company.calculate_rsi(info, period=14))
print(company.calculate_stochastic_oscillator(info, period=14))
print(company.calculate_daily_range(info))
print(company.detect_doji(info, tolerance=0.001))
print(company.detect_engulfing(info))
print(company.calculate_cumulative_return(info))
print(company.calculate_sharpe_ratio(info, risk_free_rate=0.01, period=252))
print(company.calculate_daily_returns(info))