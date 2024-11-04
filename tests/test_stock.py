import pytest
import pandas as pd
from src.Financiers.stock import Stock, BrainrotDataFrame
from datetime import datetime, timedelta

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

    # Test that Forecast Prices Function Returns a DataFrame with the Correct Structure
    def test_forecast_prices_structure(monkeypatch):
    # Mock get_price_data to provide historical data
     def mock_get_price_data(symbol_string):
        mock_price_data = pd.DataFrame({
            'date': pd.date_range(start="2023-01-01", periods=10, freq="D"),
            'price': [100.0 + i for i in range(10)]
        })
        return BrainrotDataFrame("Mock data", mock_price_data)

     stock = Stock()
     monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)

     # Call forecast_prices and check structure
     forecast = stock.forecast_prices("IBM", days=5)
    
     assert forecast.df is not None, "Forecast DataFrame should not be None"
     assert 'date' in forecast.df.columns, "Forecast DataFrame missing 'date' column"
     assert 'predicted_price' in forecast.df.columns, "Forecast DataFrame missing 'predicted_price' column"
     assert not forecast.df.empty, "Forecast DataFrame should not be empty"

    # Test for Correct Number of Forecasted Days
    def test_forecast_prices_row_count(monkeypatch):
        # Mock get_price_data to provide historical data
        def mock_get_price_data(symbol_string):
            mock_price_data = pd.DataFrame({
                'date': pd.date_range(start="2023-01-01", periods=10, freq="D"),
                'price': [100.0 + i for i in range(10)]
            })
            return BrainrotDataFrame("Mock data", mock_price_data)

        stock = Stock()
        monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)

        # Test with specified days to forecast
        days_to_forecast = 7
        forecast = stock.forecast_prices("IBM", days=days_to_forecast)

        assert len(forecast.df) == days_to_forecast, f"Expected {days_to_forecast} rows, but got {len(forecast.df)}"

    # Test for Predicted Price Range
    def test_forecast_prices_value_range(monkeypatch):
        # Mock get_price_data to provide historical data
        def mock_get_price_data(symbol_string):
            mock_price_data = pd.DataFrame({
                'date': pd.date_range(start="2023-01-01", periods=10, freq="D"),
                'price': [100.0 + i for i in range(10)]
            })
            return BrainrotDataFrame("Mock data", mock_price_data)

        stock = Stock()
        monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)

        # Generate forecast and check price range
        forecast = stock.forecast_prices("IBM", days=5)
        
        # Assert all predicted prices are within the expected range
        assert forecast.df['predicted_price'].between(100, 150).all(), "Predicted prices are not within the expected range (100, 150)"
