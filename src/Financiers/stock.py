import pandas as pd
import numpy as np
import requests
from dotenv import load_dotenv
import os
import random
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .quotes import quotes

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
    
    def get_top_movers(self, symbols):
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

