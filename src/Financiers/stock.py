import pandas as pd
import requests
from dotenv import load_dotenv
import os
import random
from Financiers.quotes import quotes
import numpy as np


load_dotenv()


class Stock:
    def __init__(self):
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY")

    # TODO: add optional argument for quarterly or annual
    def get_earnings(self, symbol_string):
        """
        Retrieves the annual and quarterly earnings (EPS) for the company of interest
        Arguments:
        symbol_string: a string representing the ticker of your choice. For example: symbol=IBM.

        Returns:
        a custom pandas DataFrame BrainrotDataFrame containing a random brainrot quote and a DataFrame with two columns 'date' and 'reportedEPS'
        """
        url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol_string}&apikey={self.api_key}"

        response = requests.get(url)
        data = response.json()

        annualEarnings = pd.DataFrame(
            data["annualEarnings"]
        )  # convert 'annualEarnings' from json (list of dictionaries orignally) into DataFrame
        annualEarnings = annualEarnings[
            ["fiscalDateEnding", "reportedEPS"]
        ]  # select only two columns, fiscalDateEnding and reportedEPS from annualEarnings df
        annualEarnings.columns = [
            "date",
            "reportedEPS",
        ]  # rename the columns for beter readability
        annualEarnings["type"] = (
            "Annual"  # added this to differentiate between quarterly earnings below vvvv
        )

        # and just do the same thing above for below for quarterly earnings cuz the API call happens to return both
        quarterlyEarnings = pd.DataFrame(data["quarterlyEarnings"])
        quarterlyEarnings = quarterlyEarnings[["fiscalDateEnding", "reportedEPS"]]
        quarterlyEarnings.columns = ["date", "reportedEPS"]
        quarterlyEarnings["type"] = "Quarterly"

        earnings_df = pd.concat(
            [annualEarnings, quarterlyEarnings], ignore_index=True
        )  # concat (combine) annual and quarterly earnings into a single df (dataframe)

        earnings_df = earnings_df.sort_values(by="date", ascending=False).reset_index(
            drop=True
        )  # sort df by date (otherwise it wasn't sorted)
        brainrot = random.choice(quotes).replace(
            "{stock}", symbol_string
        )  # get brainrot
        # return the dataframe with brainrot
        return BrainrotDataFrame(brainrot, earnings_df)
    


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
    

print("Script started.")
print("Processing complete.")

