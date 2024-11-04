import pandas as pd
import numpy as np
import requests
from dotenv import load_dotenv
import os
import random
from Financiers.quotes import quotes
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .quotes import quotes


load_dotenv()


class Stock:
    def __init__(self):
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    
    def get_market_mood(self):
        """
        Provides a random vibe check on the current market mood with brainrot and stock trends

        Returns:
        A meaningless brainrot statement about the stock market's vibe using top gainers/losers
        """
        # get the top gainers and losers data
        url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()

        # check for valid data and get top gainer/loser information
        if "top_gainers" in data and "top_losers" in data:
            # get the top gainer and top loser from the API JSOn
            top_gainer = data["top_gainers"][0]
            top_loser = data["top_losers"][0]
            
            # get data for the top gainer and top loser
            gainer_ticker = top_gainer["ticker"]
            gainer_change_percentage = top_gainer["change_percentage"]
            loser_ticker = top_loser["ticker"]
            loser_change_percentage = top_loser["change_percentage"]
        else:
            # in case of missing data
            gainer_ticker, gainer_change_percentage = "UNKNOWN", "0%"
            loser_ticker, loser_change_percentage = "UNKNOWN", "0%"

        # brainrot, courtesy of Brainrot GPT
        vibes = [
            f"The market's giving that Kai Cenat energy – {gainer_ticker} just rizzed up by {gainer_change_percentage}!",
            f"Bruh, {loser_ticker} is giving sus Grimace Shake vibes, tanked {loser_change_percentage}. Ohio level cringe.",
            f"Today, {gainer_ticker} hit skibidi highs with a {gainer_change_percentage} jump – Sigma grind paying off.",
            f"{loser_ticker} be acting real sussy with that {loser_change_percentage} drop. Total Amongus vibes.",
            f"Not gonna lie, {gainer_ticker} and {loser_ticker} are straight gooning. Market on a Phanum tax spree!",
            f"Bruh, {gainer_ticker} is flexing with a {gainer_change_percentage} gain, leaving {loser_ticker} in Ohio with a {loser_change_percentage} drop.",
            f"Market mood today? {gainer_ticker} is mogging the charts, but {loser_ticker} out here paying the Phanum tax.",
            f"{gainer_ticker} skyrocketed {gainer_change_percentage}, pure Sigma grind, while {loser_ticker} just dipped – classic cringe arc.",
            f"Today's market is edgy AF – {gainer_ticker} flexed {gainer_change_percentage}, while {loser_ticker} went sussy by {loser_change_percentage}."
        ]
        return random.choice(vibes)

    def get_earnings(self, symbol_string, annual=True, numDays=5):
        """
        Retrieves the annual and quarterly earnings (EPS) for the company of interest
        Arguments:
        symbol_string: a string representing the ticker of your choice. For example: symbol=IBM.
        annual: optional bool for whether earnings are reported quarterly or annually. default annual (True)
        numDays: optional int for how many days back you want stock data for

        Returns:
        a custom pandas DataFrame BrainrotDataFrame containing a random brainrot quote and a DataFrame with two columns 'date' and 'reportedEPS'
        """
        url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol_string}&apikey={self.api_key}"

        response = requests.get(url)
        data = response.json()
        
        if "annualEarnings" not in data or "quarterlyEarnings" not in data:
            print(f"Error: No data found for symbol '{symbol_string}'. Please check if the symbol is correct.")
            return None
        
        if annual:
            earnings = pd.DataFrame(data["annualEarnings"])
            earnings["type"] = "Annual"
        else:
            earnings = pd.DataFrame(data["quarterlyEarnings"])
            earnings["type"] = "Quarterly"

        # rename columns 
        earnings = earnings[["fiscalDateEnding", "reportedEPS"]]
        earnings.columns = ["date", "reportedEPS"]
        
        # sort     
        earnings = earnings.sort_values(by="date", ascending=False).reset_index(drop=True)
        
        if numDays is not None:
            earnings = earnings.head(numDays)
            
        # get funny brainrot quote
        brainrot = random.choice(quotes).replace("{stock}", symbol_string)
        
        return BrainrotDataFrame(brainrot, earnings)
   
    def get_price_data(self, symbol_string):
        """
        Retrieves daily stock price data for the specified symbol.
        Arguments:
        symbol_string: Stock ticker as a string.

        Returns:
        BrainrotDataFrame containing the historical price data.
        """
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_string}&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()

        # Process JSON response to DataFrame
        time_series = data.get("Time Series (Daily)", {})
        price_data = pd.DataFrame({
            "date": pd.to_datetime(list(time_series.keys())),
            "price": [float(value["4. close"]) for value in time_series.values()]
        }).sort_values(by="date")

        brainrot = f"Historical prices for {symbol_string}. Embrace the data!"
        return BrainrotDataFrame(brainrot, price_data)

    def forecast_prices(self, symbol_string, days=30):
        """
        Forecasts stock prices using a simple model.
        Arguments:
        symbol_string: stock ticker.
        days: how far into the future to forecast (default: 30 days).

        Returns:
        A DataFrame with forecasted dates and predicted prices.
            """
        price_data = self.get_price_data(symbol_string).df
        # Placeholder for ARIMA or similar forecasting model
        forecasted_prices = [random.uniform(100, 150) for _ in range(days)]  # Mock data
        forecast_df = pd.DataFrame({
            'date': pd.date_range(start=price_data['date'].max(), periods=days + 1, freq='D')[1:],
            'predicted_price': forecasted_prices
        })

        brainrot = f"{days}-day forecast for {symbol_string}. Is this sigma behavior?"
        return BrainrotDataFrame(brainrot, forecast_df)
    
    def company_overview(self,symbol_string):
        """
        Provides general company overview
        Arguments:
        symbol_string: stock ticker.

        Returns:
        Returns a Company object with relevant information.
        """
        if not symbol_string:
            print("Error: No symbol provided.")
            return None
        
        url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol_string}&apikey={self.api_key}"
        
        try: 
            response = requests.get(url)
            data = response.json()

            #exception handling
            if not data or "Symbol" not in data:
                print(f"Error: No data found for symbol '{symbol_string}'. Please check if the symbol is correct.")
                return None
        
            companyObj = Company(data)
            
            brainrot = random.choice(quotes).replace(
                "{stock}", symbol_string
            ) 
            
            # return the Company object with brainrot
            return BrainrotWrapper(brainrot, companyObj)
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to AlphaVantage API. Check your network connection.")
        except requests.exceptions.Timeout:
            print("Error: The request to AlphaVantage API timed out.")
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
        except ValueError:
            print("Error: Received invalid JSON response from AlphaVantage API.")
        return None
    
    def plot_top_movers(self, symbols):
        """
        Retrieves and displays the top gainer and loser among the provided stock symbols.
        Arguments:
        symbols: List of stock tickers.

        Returns:
        BrainrotDataFrame with two DataFrames for the top gainer and loser including the percent change and plots.
        """
        movers_data = []
        for symbol in symbols:
            price_data = self.get_price_data(symbol).df
            if not price_data.empty:
                percent_change = ((price_data['price'].iloc[-1] - price_data['price'].iloc[0]) / price_data['price'].iloc[0]) * 100
                movers_data.append((symbol, percent_change, price_data))

        if not movers_data:
            return "No data available for the provided symbols."

        top_gainer = max(movers_data, key=lambda x: x[1])
        top_loser = min(movers_data, key=lambda x: x[1])

        # Generate a brainrot quote for the title
        brainrot_quote = random.choice(quotes).replace("{stock}", f"{top_gainer[0]} and {top_loser[0]}")
        
        # Plotting top gainer and loser with brainrot quotes as titles
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))
        
        ax[0].plot(top_gainer[2]['date'], top_gainer[2]['price'])
        ax[0].set_title(f"Top Gainer: {top_gainer[0]} with {top_gainer[1]:.2f}% Change\n{brainrot_quote}")
        
        ax[1].plot(top_loser[2]['date'], top_loser[2]['price'])
        ax[1].set_title(f"Top Loser: {top_loser[0]} with {top_loser[1]:.2f}% Change\n{brainrot_quote}")
        
        plt.tight_layout()
        plt.show()

        # Return the top gainer and loser data with the brainrot as a custom DataFrame
        data = {
            "Top Gainer": {"Symbol": top_gainer[0], "Percent Change": top_gainer[1]},
            "Top Loser": {"Symbol": top_loser[0], "Percent Change": top_loser[1]}
        }
        
        return BrainrotDataFrame(brainrot_quote, pd.DataFrame(data))

    def project_future_estimates(self, symbols, days=30, pattern="neutral"):
        """
        Provides future estimates for each stock in the given list over a specified number of days.
        Arguments:
        symbols: List of stock tickers.
        days: Number of days to forecast (default: 30).
        pattern: Trend pattern for the forecast - can be "bullish", "bearish", or "neutral".

        Returns:
        BrainrotDataFrame with a DataFrame of forecasted prices for each symbol.
        """
        if not symbols:
            # Return an empty BrainrotDataFrame if no symbols are provided
            empty_df = pd.DataFrame(columns=["date", "predicted_price", "Symbol"])
            brainrot_quote = "No symbols provided for forecast."
            return BrainrotDataFrame(brainrot_quote, empty_df)

        forecasts = []
        for symbol in symbols:
            forecast_df = self.forecast_prices(symbol, days=days).df

            # Apply the pattern to adjust the forecasted prices
            if pattern.lower() == "bullish":
                # Simulate an upward trend by incrementally increasing prices
                forecast_df["predicted_price"] = forecast_df["predicted_price"] * (1 + 0.01 * forecast_df.index)
            elif pattern.lower() == "bearish":
                # Simulate a downward trend by incrementally decreasing prices
                forecast_df["predicted_price"] = forecast_df["predicted_price"] * (1 - 0.01 * forecast_df.index)
            elif pattern.lower() == "neutral":
                # Keep prices relatively stable with minor random fluctuations
                forecast_df["predicted_price"] += [random.uniform(-1, 1) for _ in range(days)]
            
            forecast_df["Symbol"] = symbol
            forecasts.append(forecast_df)

        combined_forecasts = pd.concat(forecasts, ignore_index=True)
        
        # Fun quote with the chosen pattern
        brainrot_quote = f"Future estimates with a {pattern} outlook for the next {days} days – hope it's accurate!"
        
        return BrainrotDataFrame(brainrot_quote, combined_forecasts)
    
    def Stockprice_getter(self, stock_name):
        """
        Retrieve raw (as-traded) daily time series (date, daily open, daily high, daily low, daily 
        close, daily volume) of the global equity specified, covering latest 100 data points

        Return: 
                Price Trends and Moving Averages
                - **Simple Moving Average (SMA):** Calculate the average of the closing price over a rolling window (e.g., 20-day SMA, 50-day SMA) to identify trends and potential support or resistance levels.
                - **Exponential Moving Average (EMA):** The EMA gives more weight to recent prices, making it useful to catch recent trends.
                - **Crossovers:** When a short-term SMA or EMA crosses a longer-term one (e.g., 20-day EMA crossing 50-day EMA), it may indicate a potential change in trend (bullish or bearish signal).
        """

        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&outputsize=compact&datatype=csv&apikey={self.api_key}"
        r = requests.get(url)
        data = r.csv()
    
    ### 1. **Price Trends and Moving Averages**
    ###Simple Moving Average (SMA):** Calculate the average of the closing price over a rolling window (e.g., 20-day SMA, 50-day SMA) to identify trends and potential support or resistance levels.
    ###Exponential Moving Average (EMA):** The EMA gives more weight to recent prices, making it useful to catch recent trends.
    ###Crossovers:** When a short-term SMA or EMA crosses a longer-term one (e.g., 20-day EMA crossing 50-day EMA), it may indicate a potential change in trend (bullish or bearish signal).
    def calculate_sma(self, data, window=20):
        """
        Calculate the Simple Moving Average (SMA) over a specified window.
        
        Parameters:
            data (pd.DataFrame): DataFrame with 'close' prices.
            window (int): The window size for SMA (default is 20).
        
        Returns:
            pd.Series: A Series with SMA values.
        """
        return data['close'].rolling(window=window).mean()

    def calculate_ema(self, data, span=20):
        """
        Calculate the Exponential Moving Average (EMA) over a specified span.
        
        Parameters:
            data (pd.DataFrame): DataFrame with 'close' prices.
            span (int): The span for EMA (default is 20).
        
        Returns:
            pd.Series: A Series with EMA values.
        """
        return data['close'].ewm(span=span, adjust=False).mean()
    
    def detect_crossover(self, short_term, long_term):
        """
        Detect when a crossover occurs between short-term and long-term moving averages.
        
        Parameters:
            short_term (pd.Series): Short-term moving average (SMA or EMA).
            long_term (pd.Series): Long-term moving average (SMA or EMA).
        
        Returns:
            pd.Series: A Series indicating crossovers:
                    - 1 for bullish crossover,
                    - -1 for bearish crossover,
                    - 0 otherwise.
        """
        crossover = pd.Series(0, index=short_term.index)
        crossover[short_term > long_term] = 1  # Bullish crossover
        crossover[short_term < long_term] = -1  # Bearish crossover
        return crossover.diff()  # Highlights where crossover occurs
    
    ### 2. **Volatility Measurement**
    ### Standard Deviation (σ):** Measure the standard deviation of daily returns to understand price volatility. Higher volatility can indicate higher risk.
    ### Average True Range (ATR):** The ATR uses the high, low, and close prices to capture average daily volatility over a specified period.

    def calculate_rolling_std(self, data, window=20):
        def calculate_daily_returns(data):
            """
            Calculate daily returns based on closing prices.
            
            Parameters:
                data (pd.DataFrame): DataFrame containing 'close' prices.
            
            Returns:
                pd.Series: A Series with daily returns.
            """
            return data['close'].pct_change()
        
        """
        Calculate the rolling standard deviation of daily returns to measure volatility.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' prices.
            window (int): The window size for calculating rolling standard deviation (default is 20).
        
        Returns:
            pd.Series: A Series with rolling standard deviation values.
        """
        daily_returns = calculate_daily_returns(data)
        return daily_returns.rolling(window=window).std()
    
    def calculate_atr(self, data, window=14):
        def calculate_true_range(data):
            """
            Calculate the True Range (TR) for each day.
            
            Parameters:
                data (pd.DataFrame): DataFrame containing 'high', 'low', and 'close' prices.
            
            Returns:
                pd.Series: A Series with True Range values.
            """
            high_low = data['high'] - data['low']
            high_close = np.abs(data['high'] - data['close'].shift())
            low_close = np.abs(data['low'] - data['close'].shift())
            true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
            return true_range
        
        """
        Calculate the Average True Range (ATR) over a specified window.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'high', 'low', and 'close' prices.
            window (int): The window size for calculating ATR (default is 14).
        
        Returns:
            pd.Series: A Series with ATR values.
        """
        true_range = calculate_true_range(data)
        return true_range.rolling(window=window).mean()
    
    ### 3.Price Momentum and Rate of Change (ROC)
    ###Momentum: Directly measures the price difference over a set period, providing a straightforward signal of price direction.
    ###Rate of Change (ROC): Provides the percentage change, indicating the pace of the price movement, which can signal if a stock is potentially overbought (high ROC) or oversold (low ROC).

    def calculate_momentum(self, data, period=10):
        """
        Calculate the momentum of the closing price over a specified period.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' prices.
            period (int): The period over which to calculate momentum (default is 10).
        
        Returns:
            pd.Series: A Series with momentum values.
        """
        return data['close'] - data['close'].shift(period)
    
    def calculate_roc(self, data, period=10):
        """
        Calculate the Rate of Change (ROC) of the closing price over a specified period.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' prices.
            period (int): The period over which to calculate ROC (default is 10).
        
        Returns:
            pd.Series: A Series with ROC values.
        """
        return ((data['close'] - data['close'].shift(period)) / data['close'].shift(period)) * 100

    ### 4.Volume Analysis
    ### Volume Moving Average: Highlights significant changes in volume over time, which can suggest changes in trading interest and potential buy or sell pressure.
    ### Volume Price Trend (VPT):Combines volume with price changes, adding context to the volume spikes, which can confirm or diverge from the price trend.
    def calculate_volume_moving_average(self, data, window=20):
        """
        Calculate the moving average of the volume over a specified window.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'volume'.
            window (int): The window size for the volume moving average (default is 20).
        
        Returns:
            pd.Series: A Series with volume moving average values.
        """
        return data['volume'].rolling(window=window).mean()

    def calculate_vpt(self, data):
        """
        Calculate the Volume Price Trend (VPT).
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' and 'volume' columns.
        
        Returns:
            pd.Series: A Series with VPT values.
        """
        # Calculate daily price change as a percentage
        daily_price_change = data['close'].pct_change()
        # Calculate VPT: Volume * price change percentage (cumulative sum)
        vpt = (data['volume'] * daily_price_change).cumsum()
        return vpt

    ### 5.Volatility and Bollinger Bands
    ### Bollinger Bands:
            #Price near the upper band: Indicates potential overbought conditions, which may signal a reversal or a pullback.
            #Price near the lower band: Indicates potential oversold conditions, which may signal a bounce or upward movement.
    
    def calculate_bollinger_bands(self, data, window=20, num_std_dev=2):
        """
        Calculate Bollinger Bands (upper and lower bands around a moving average).
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' prices.
            window (int): The window size for the moving average (default is 20).
            num_std_dev (int): The number of standard deviations for the bands (default is 2).
        
        Returns:
            pd.DataFrame: A DataFrame with columns for the moving average (MA),
                        upper band, and lower band.
        """
        # Calculate the simple moving average (SMA)
        sma = data['close'].rolling(window=window).mean()
        
        # Calculate the rolling standard deviation
        rolling_std = data['close'].rolling(window=window).std()
        
        # Calculate upper and lower Bollinger Bands
        upper_band = sma + (rolling_std * num_std_dev)
        lower_band = sma - (rolling_std * num_std_dev)
        
        # Combine everything into a single DataFrame
        bollinger_bands = pd.DataFrame({
            'sma': sma,
            'upper_band': upper_band,
            'lower_band': lower_band
        })
        
        return bollinger_bands

    ### 6.Price Oscillators and Indicators
    ### RSI: Measures the strength of recent price changes. By analyzing RSI values, you can identify potential reversal points:
        ### RSI > 70: Possible overbought, indicating a price reversal or correction.
        ### RSI < 30: Possible oversold, indicating a potential buying opportunity.
    ### Stochastic Oscillator: Compares the closing price to the price range over a specified period.
        ### Value > 80: Indicates overbought conditions.
        ### Value < 20: Indicates oversold conditions.

    def calculate_rsi(self, data, period=14):
        """
        Calculate the Relative Strength Index (RSI).
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' prices.
            period (int): The period over which to calculate RSI (default is 14).
        
        Returns:
            pd.Series: A Series with RSI values.
        """
        delta = data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_stochastic_oscillator(self, data, period=14):
        """
        Calculate the Stochastic Oscillator.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'high', 'low', and 'close' prices.
            period (int): The period over which to calculate the oscillator (default is 14).
        
        Returns:
            pd.Series: A Series with Stochastic Oscillator values.
        """
        lowest_low = data['low'].rolling(window=period).min()
        highest_high = data['high'].rolling(window=period).max()
        stochastic = 100 * ((data['close'] - lowest_low) / (highest_high - lowest_low))
        return stochastic
    
    ### 7.Price Spreads and Candlestick Patterns**
    ### Daily Range: Helps analyze daily price fluctuations, which can serve as a volatility measure.
    ### Doji Pattern: Often signals indecision and can indicate a potential reversal if it appears after a strong trend.
    ###Engulfing Pattern:
        ###Bullish Engulfing: Indicates potential bullish reversal, where the larger second candlestick suggests increased buying pressure.
        ###Bearish Engulfing: Indicates potential bearish reversal, with the larger second candlestick showing increased selling pressure.
    
    def calculate_daily_range(self, data):
        """
        Calculate the daily range (High - Low).
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'high' and 'low' prices.
        
        Returns:
            pd.Series: A Series with daily range values.
        """
        return data['high'] - data['low']
    
    def detect_doji(self, data, tolerance=0.001):
        """
        Detect Doji candlestick patterns where the open and close prices are very close.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'open' and 'close' prices.
            tolerance (float): The tolerance level to consider open and close as equal (default is 0.001).
        
        Returns:
            pd.Series: A Series indicating the presence of a Doji pattern (True/False).
        """
        return abs(data['close'] - data['open']) <= tolerance * data['close']

    def detect_engulfing(self, data):
        """
        Detect Engulfing candlestick patterns (bullish and bearish).
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'open', 'close', 'high', and 'low' prices.
        
        Returns:
            pd.Series: A Series with values:
                    - 1 for a bullish engulfing pattern,
                    - -1 for a bearish engulfing pattern,
                    - 0 otherwise.
        """
        # Detect bullish engulfing
        bullish = (data['open'].shift(1) > data['close'].shift(1)) & (data['open'] < data['close']) & \
                (data['open'] < data['close'].shift(1)) & (data['close'] > data['open'].shift(1))
        
        # Detect bearish engulfing
        bearish = (data['open'].shift(1) < data['close'].shift(1)) & (data['open'] > data['close']) & \
                (data['open'] > data['close'].shift(1)) & (data['close'] < data['open'].shift(1))
        
        pattern = pd.Series(0, index=data.index)
        pattern[bullish] = 1   # Bullish Engulfing
        pattern[bearish] = -1  # Bearish Engulfing
        
        return pattern
    
    ### 8. **Returns Analysis and Risk Metrics**
    ### Daily Returns: Shows daily percentage changes, which can reveal day-to-day volatility.
    ### Cumulative Return: Provides a longer-term view, showing the overall percentage change from the start to the end of the period.
    ### Sharpe Ratio: Evaluates the risk-adjusted return, helping assess the efficiency of the investment relative to its risk. A higher Sharpe Ratio indicates better risk-adjusted performance.

    def calculate_cumulative_return(self, data):
        """
        Calculate the cumulative return over the entire period.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' prices.
        
        Returns:
            float: Cumulative return as a percentage.
        """
        cumulative_return = (data['close'].iloc[-1] / data['close'].iloc[0]) - 1
        return cumulative_return * 100
    
    def calculate_sharpe_ratio(self, data, risk_free_rate=0.01, period=252):
        def calculate_daily_returns(data):
            """
            Calculate daily returns based on closing prices.
            
            Parameters:
                data (pd.DataFrame): DataFrame containing 'close' prices.
            
            Returns:
                pd.Series: A Series with daily return values.
            """
            return data['close'].pct_change()

        """
        Calculate the Sharpe Ratio for a given period.
        
        Parameters:
            data (pd.DataFrame): DataFrame containing 'close' prices.
            risk_free_rate (float): Risk-free rate of return (default is 0.01 or 1%).
            period (int): Number of trading days in a year (default is 252 for daily data).
        
        Returns:
            float: The Sharpe Ratio.
        """
        daily_returns = calculate_daily_returns(data)
        excess_return = daily_returns.mean() * period - risk_free_rate
        return excess_return / (daily_returns.std() * (period ** 0.5))

    
class Company:
    def __init__(self, CompanyJsonObj):
        self.symbol = CompanyJsonObj['Symbol']
        self.name = CompanyJsonObj['Name']
        self.description = CompanyJsonObj['Description']
        self.CIK = CompanyJsonObj['CIK']
        self.country = CompanyJsonObj['Country']
        self.sector = CompanyJsonObj['Sector']
        self.industry = CompanyJsonObj['Industry']
        

    def __str__(self):
        return (
            f"Company Information:\n"
            f"Symbol: {self.symbol}\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"CIK: {self.CIK}\n"
            f"Country: {self.country}\n"
            f"Sector: {self.sector}\n"
            f"Industry: {self.industry}"
        )
    
    def forecast_by_date_range(self, date_range="last_month", days_to_forecast=30, model_type="linear",
                           confidence_level=0.95, frequency="daily", return_format="dataframe"):
        """
        Generates a forecast based on historical data within a specified date range and forecasting model.

        Arguments:
        date_range: str - Specifies the range ("last_day", "last_month", "last_year").
        days_to_forecast: int - Number of future days to forecast.
        model_type: str - Type of forecasting model ("linear", "random_walk").
        confidence_level: float - Confidence level for forecast intervals (e.g., 0.95 for 95%).
        frequency: str - Frequency of forecasted data points ("daily", "weekly", "monthly").
        return_format: str - Output format ("dataframe" or "json").

        Returns:
        BrainrotDataFrame or JSON with forecasted dates and prices (and confidence intervals, if applicable).
        """
        today = datetime.today()

        # Define the start date based on the date range
        if date_range == "last_day":
            start_date = today - timedelta(days=1)
        elif date_range == "last_month":
            start_date = today - timedelta(days=30)
        elif date_range == "last_year":
            start_date = today - timedelta(days=365)
        else:
            raise ValueError("Invalid date range. Choose from 'last_day', 'last_month', or 'last_year'.")

        # Generate mock historical data for the specified date range
        date_range_days = (today - start_date).days
        historical_dates = pd.date_range(start=start_date, end=today, freq='D')
        historical_prices = [100 + i * 0.5 + random.uniform(-2, 2) for i in range(date_range_days + 1)]
        earnings_df = earnings_df.sort_values(by="date", ascending=False).reset_index(
            drop=True
        )  # sort df by date (otherwise it wasn't sorted)
        brainrot = random.choice(quotes).replace(
            "{stock}", symbol_string
        )  # get brainrot
        # return the dataframe with brainrot
        return BrainrotDataFrame(brainrot, earnings_df)
    


    


      
      
        historical_df = pd.DataFrame({
            "date": historical_dates,
            "price": historical_prices
        })

        # Forecast based on the selected model
        last_price = historical_df["price"].iloc[-1]
        forecasted_dates = pd.date_range(start=today + timedelta(days=1), periods=days_to_forecast, freq=frequency[0].upper())

        if model_type == "linear":
            # Simple linear trend
            forecasted_prices = [last_price + i * 0.5 for i in range(1, days_to_forecast + 1)]
        elif model_type == "random_walk":
            # Random walk around the last price
            forecasted_prices = [last_price + random.uniform(-2, 2) for _ in range(days_to_forecast)]
        else:
            raise ValueError("Invalid model type. Choose 'linear' or 'random_walk'.")

        # Calculate confidence intervals if requested
        if confidence_level:
            std_dev = np.std(forecasted_prices)
            lower_bound = [price - 1.96 * std_dev for price in forecasted_prices]
            upper_bound = [price + 1.96 * std_dev for price in forecasted_prices]
            forecast_df = pd.DataFrame({
                "date": forecasted_dates,
                "predicted_price": forecasted_prices,
                "lower_bound": lower_bound,
                "upper_bound": upper_bound
            })
        else:
            forecast_df = pd.DataFrame({
                "date": forecasted_dates,
                "predicted_price": forecasted_prices
            })

        # Add a brainrot quote based on forecast details
        brainrot_quote = random.choice(quotes).format(
            stock=self.symbol,  # Changed to match {stock} placeholder in quotes.py
            confidence=int(confidence_level * 100),
            model_type=model_type,
            date_range=date_range.replace('_', ' ')
        )

        # Return in specified format with the brainrot quote
        if return_format == "json":
            return {"quote": brainrot_quote, "data": forecast_df.to_dict(orient="records")}
        return BrainrotDataFrame(brainrot_quote, forecast_df)
        
class BrainrotDataFrame:
    """
    A custom DataFrame wrapper class that adds brainrot quote above the DataFrame output
    """
    def __init__(self, quote, df):
        self.quote = quote
        self.df = df

    def __str__(self):
        return f"{self.quote}\n\n{self.df}"  # have it so the brainrot appears, newline, then the dataframe

    def __repr__(self):
        return self.__str__()

class BrainrotWrapper:
    """
    A custom wrapper class that adds brainrot quote above the original output
    """
    def __init__(self, quote, object):
        self.quote = quote
        self.object = object

    def __str__(self):
        return f"{self.quote}\n\n{self.object}"  # have it so the brainrot appears, newline, then the dataframe

    def __repr__(self):
        return self.__str__()
    

print("Script started.")
print("Processing complete.")

