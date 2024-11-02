import pytest
import pandas as pd
from src.Financiers.stock import Stock, BrainrotDataFrame
from unittest.mock import patch
import random

class Tests:
    
    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python -m pytest -s` command to run all tests with print statements (-s) if u include them
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be True!"
        
    def test_get_earnings(self):
        print("\n Testing get_earnings() with IBM")
        stock = Stock()
        earnings = stock.get_earnings("IBM")
        
        # assert df has correct columns
        expected_columns = ['date', 'reportedEPS', 'type']
        assert list(earnings.df.columns) == expected_columns, "DataFrame columns do not match expected columns"
        
        # checkign df is not empty
        assert not earnings.df.empty, "Earnings DataFrame is empty, but it was expected to contain data"

    @patch('src.Financiers.stock.Stock.get_price_data')
    def test_forecast_prices(self, mock_get_price_data):
        print("\nTesting forecast_prices() with mocked data")
        stock = Stock()
        symbol = "AAPL"
        days = 30
        
        # Mock the get_price_data method to return controlled data
        mock_data = pd.DataFrame({
            'date': pd.date_range(start="2023-01-01", periods=100, freq='D'),
            'close': [random.uniform(100, 150) for _ in range(100)]
        })
        mock_get_price_data.return_value = BrainrotDataFrame("Mocked quote", mock_data)

        # Call forecast_prices
        forecast = stock.forecast_prices(symbol, days)

        # Check that the return type is BrainrotDataFrame
        assert isinstance(forecast, BrainrotDataFrame), "Expected a BrainrotDataFrame as the return type"

        # Check the DataFrame columns
        assert "date" in forecast.df.columns, "Expected 'date' column in forecast DataFrame"
        assert "predicted_price" in forecast.df.columns, "Expected 'predicted_price' column in forecast DataFrame"
        
        # Verify the number of rows matches the number of forecast days
        assert len(forecast.df) == days, f"Expected {days} rows in forecast DataFrame, got {len(forecast.df)}"

        # Ensure that all predicted prices are within the specified range
        within_range = forecast.df["predicted_price"].between(100, 150).all()
        assert within_range, "All predicted_price values should be between 100 and 150"

        # Check that the forecast message includes the stock symbol and days
        assert f"{days}-day forecast for {symbol}" in forecast.quote, "Expected forecast quote to contain symbol and days"
