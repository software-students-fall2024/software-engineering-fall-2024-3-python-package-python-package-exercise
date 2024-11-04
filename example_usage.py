from Financiers.stock import Stock

stock = Stock()

print(stock.get_market_mood())
print (stock.get_earnings("AAPL"))
print(stock.get_price_data("AAPL"))
print(stock.forecast_prices("AAPL"))
print(stock.company_overview("IBM"))
print(stock.plot_top_movers(["AAPL", "GOOGL","IBM"]))
print(stock.project_future_estimates(["AAPL", "GOOGL","IBM"]))

data = {
    'high': [10, 10, 12, 12, 12, 12, 12, 12, 12, 12],
    'low': [8, 8, 9, 10, 10, 10, 10, 10, 10, 10],
    'close': [9, 9, 10, 11, 11, 11, 11, 11, 11, 11]
}
print(stock.calculate_atr(data))

