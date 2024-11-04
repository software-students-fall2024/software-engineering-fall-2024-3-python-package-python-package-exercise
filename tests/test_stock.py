import pytest
import pandas as pd
import unittest
from unittest.mock import patch
from io import StringIO
from src.Financiers.stock import Stock, Company, BrainrotDataFrame, BrainrotWrapper
from datetime import datetime, timedelta
import numpy as np
import random
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
class MockResponse:
    def __init__(self, status_code, json={}):
        self.status_code = status_code
        self.result_json = json
    def json(self):
        return self.result_json
    
# the fixture for the mock IBM data (so we don't have to keep API calling in tests)
@pytest.fixture
def ibm_mock_data():
    return {
        "symbol": "IBM",
        "annualEarnings": [
            {"fiscalDateEnding": "2022-12-31", "reportedEPS": "12.34"},
            {"fiscalDateEnding": "2021-12-31", "reportedEPS": "10.12"},
            {"fiscalDateEnding": "2020-12-31", "reportedEPS": "8.90"},
            {"fiscalDateEnding": "2019-12-31", "reportedEPS": "7.45"},
            {"fiscalDateEnding": "2018-12-31", "reportedEPS": "6.78"}
        ],
        "quarterlyEarnings": [
            {"fiscalDateEnding": "2022-12-31", "reportedEPS": "3.21"},
            {"fiscalDateEnding": "2022-09-30", "reportedEPS": "2.98"}
        ]
    }

@pytest.fixture
def mock_get(monkeypatch, ibm_mock_data):
    def mock_request_get(*args, **kwargs):
        return MockResponse(200, ibm_mock_data)
    monkeypatch.setattr("requests.get", mock_request_get)


class Tests:
    
    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python -m pytest -s` command to run all tests with print statements (-s) if u include them
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be True!"

    def setUp(self):
        # Assuming the Stock class is initialized with an API key attribute.
        self.stock = Stock(api_key="YOUR_API_KEY")  # replace with actual API key
        self.trade_info = self.stock.Stockprice_getter("AAPL")

    def test_Stockprice_getter(self):
        print("\nTesting Stockprice_getter() with AAPL")

        # Check that the data has the correct columns
        expected_columns = ["timestamp", "open", "high", "low", "close", "volume"]
        self.assertListEqual(list(self.trade_info.columns), expected_columns, "Columns do not match expected format")

        # Check data is not empty
        self.assertFalse(self.trade_info.empty, "Data returned is empty")

        # Check that there are at least 100 data points as expected
        self.assertGreaterEqual(len(self.trade_info), 100, "Data should contain at least 100 data points")

    def test_calculate_sma(self):
        print("\nTesting calculate_sma()")

        # Check that the SMA function returns a non-empty Series
        result_sma = self.stock.calculate_sma(self.trade_info, window=20)
        self.assertFalse(result_sma.empty, "SMA result should not be empty for input data")

        # Check that the SMA result length matches input data length
        self.assertEqual(len(result_sma), len(self.trade_info), "SMA result length should match input data length")

        # Check that the first 19 values are NaN
        self.assertTrue(result_sma[:19].isna().all(), "First 19 values should be NaN due to window size")

    def test_calculate_ema(self):
        print("\nTesting calculate_ema()")

        # Check that the EMA function returns a non-empty Series
        result_ema = self.stock.calculate_ema(self.trade_info, span=20)
        self.assertFalse(result_ema.empty, "EMA result should not be empty for input data")

        # Check that the EMA result length matches input data length
        self.assertEqual(len(result_ema), len(self.trade_info), "EMA result length should match input data length")

        # Check that the first value is NaN
        self.assertTrue(pd.isna(result_ema.iloc[0]), "First EMA value should be NaN due to exponential calculation")

    def test_detect_crossover(self):
        print("\nTesting detect_crossover()")

        # Use short and long SMAs for crossover detection
        short_sma = self.stock.calculate_sma(self.trade_info, window=10)
        long_sma = self.stock.calculate_sma(self.trade_info, window=50)
        result_crossover = self.stock.detect_crossover(short_sma, long_sma)

        # Check that crossover result is not empty
        self.assertFalse(result_crossover.empty, "Crossover result should not be empty")

        # Check if crossover Series has the same length as input data
        self.assertEqual(len(result_crossover), len(short_sma), "Crossover result length should match input data length")

        # Check that crossover values are -1, 0, or 1
        self.assertTrue(result_crossover.isin([-1, 0, 1]).all(), "Crossover values should be -1, 0, or 1")

    def test_calculate_rolling_std(self):
        print("\nTesting calculate_rolling_std()")

        # Check that rolling standard deviation function returns non-empty Series
        result_std = self.stock.calculate_rolling_std(self.trade_info, window=20)
        self.assertFalse(result_std.empty, "Rolling standard deviation result should not be empty")

        # Check that the result length matches input data length
        self.assertEqual(len(result_std), len(self.trade_info), "Rolling standard deviation result length should match input data length")

        # Check that the first 19 values are NaN due to window size
        self.assertTrue(result_std[:19].isna().all(), "First 19 values should be NaN due to window size")

    def test_calculate_atr(self):
        print("\nTesting calculate_atr()")

        # Check that ATR function returns a non-empty Series
        result_atr = self.stock.calculate_atr(self.trade_info, window=14)
        self.assertFalse(result_atr.empty, "ATR result should not be empty")

        # Check that the ATR result has the same length as input data
        self.assertEqual(len(result_atr), len(self.trade_info), "ATR result length should match input data length")

        # Check that the first 13 values are NaN due to window size
        self.assertTrue(result_atr[:13].isna().all(), "First 13 values should be NaN due to window size")

    def test_calculate_momentum(self):
        print("\nTesting calculate_momentum()")

        # Check that momentum function returns a non-empty Series
        result_momentum = self.stock.calculate_momentum(self.trade_info, period=10)
        self.assertFalse(result_momentum.empty, "Momentum result should not be empty")

        # Check that the momentum result has the same length as input data
        self.assertEqual(len(result_momentum), len(self.trade_info), "Momentum result length should match input data length")

        # Check that the first 9 values are NaN due to period size
        self.assertTrue(result_momentum[:9].isna().all(), "First 9 values should be NaN due to period size")

    def test_calculate_roc(self):
        print("\nTesting calculate_roc()")

        # Check that ROC function returns a non-empty Series
        result_roc = self.stock.calculate_roc(self.trade_info, period=10)
        self.assertFalse(result_roc.empty, "ROC result should not be empty")

        # Check that the ROC result has the same length as input data
        self.assertEqual(len(result_roc), len(self.trade_info), "ROC result length should match input data length")

        # Check that the first 9 values are NaN due to period size
        self.assertTrue(result_roc[:9].isna().all(), "First 9 values should be NaN due to period size")

    def test_calculate_volume_moving_average(self):
        print("\nTesting calculate_volume_moving_average()")

        # Check that volume moving average function returns a non-empty Series
        result_volume_ma = self.stock.calculate_volume_moving_average(self.trade_info, window=20)
        self.assertFalse(result_volume_ma.empty, "Volume Moving Average result should not be empty")

        # Check that the volume moving average result has the same length as input data
        self.assertEqual(len(result_volume_ma), len(self.trade_info), "Volume Moving Average result length should match input data length")

        # Check that the first 19 values are NaN due to window size
        self.assertTrue(result_volume_ma[:19].isna().all(), "First 19 values should be NaN due to window size")

    def test_calculate_vpt(self):
        print("\nTesting calculate_vpt()")

        # Check that VPT function returns a non-empty Series
        result_vpt = self.stock.calculate_vpt(self.trade_info)
        self.assertFalse(result_vpt.empty, "VPT result should not be empty")

        # Check that the VPT result has the same length as input data
        self.assertEqual(len(result_vpt), len(self.trade_info), "VPT result length should match input data length")

        # Check that the first value is NaN due to pct_change
        self.assertTrue(pd.isna(result_vpt.iloc[0]), "First VPT value should be NaN due to percentage change")

    def test_calculate_bollinger_bands(self):
        print("\nTesting calculate_bollinger_bands()")

        # Calculate Bollinger Bands and check for non-empty result
        result_bollinger = self.stock.calculate_bollinger_bands(self.trade_info, window=20, num_std_dev=2)
        self.assertFalse(result_bollinger.empty, "Bollinger Bands result should not be empty")

        # Check that the Bollinger Bands result has the correct columns
        self.assertListEqual(list(result_bollinger.columns), ['sma', 'upper_band', 'lower_band'], "Bollinger Bands columns do not match expected format")

        # Check that the result has the same length as input data
        self.assertEqual(len(result_bollinger), len(self.trade_info), "Bollinger Bands result length should match input data length")

    def test_calculate_rsi(self):
        print("\nTesting calculate_rsi()")

        # Calculate RSI and check for non-empty result
        result_rsi = self.stock.calculate_rsi(self.trade_info, period=14)
        self.assertFalse(result_rsi.empty, "RSI result should not be empty")

        # Check that the RSI result has the same length as input data
        self.assertEqual(len(result_rsi), len(self.trade_info), "RSI result length should match input data length")

        # Check that RSI values are between 0 and 100
        self.assertTrue(result_rsi.between(0, 100).all(), "RSI values should be between 0 and 100")

    def test_calculate_daily_range(self):
        print("\nTesting calculate_daily_range()")

        # Check that daily range function returns a non-empty Series
        result_daily_range = self.stock.calculate_daily_range(self.trade_info)
        self.assertFalse(result_daily_range.empty, "Daily Range result should not be empty")

        # Check that daily range result has the same length as input data
        self.assertEqual(len(result_daily_range), len(self.trade_info), "Daily Range result length should match input data length")

        # Check that all daily range values are non-negative
        self.assertTrue((result_daily_range >= 0).all(), "Daily range values should be non-negative")

    def test_calculate_cumulative_return(self):
        print("\nTesting calculate_cumulative_return()")

        # Check that cumulative return function returns a valid result
        result_cumulative_return = self.stock.calculate_cumulative_return(self.trade_info)
        self.assertIsNotNone(result_cumulative_return, "Cumulative return should not be None")

        # Check that cumulative return is a numeric value
        self.assertIsInstance(result_cumulative_return, (float, int), "Cumulative return should be a float or int")

    def test_calculate_sharpe_ratio(self):
        print("\nTesting calculate_sharpe_ratio()")

        # Check that Sharpe Ratio function returns a valid result
        result_sharpe_ratio = self.stock.calculate_sharpe_ratio(self.trade_info)
        self.assertIsNotNone(result_sharpe_ratio, "Sharpe Ratio should not be None")

        # Check that Sharpe Ratio is a numeric value
        self.assertIsInstance(result_sharpe_ratio, (float, int), "Sharpe Ratio should be a float or int")

        
    def test_get_earnings_numDays(self, mock_get, ibm_mock_data):
        stock = Stock()

        # Test with numDays=None (should return all available entries)
        earnings_all = stock.get_earnings("IBM", annual=True, numDays=None)
        assert earnings_all is not None, "Expected a BrainrotDataFrame to be returned but got None"
        assert len(earnings_all.df) == len(ibm_mock_data["annualEarnings"]), "Expected all annual earnings entries"

        # Test with specific numDays as 3
        test_numDays = 3
        earnings_limited = stock.get_earnings("IBM", annual=True, numDays=test_numDays)
        assert earnings_limited is not None, "Expected a BrainrotDataFrame to be returned but got None"
        assert len(earnings_limited.df) == test_numDays, f"Expected {test_numDays} rows, got {len(earnings_limited.df)}"
        
    def test_get_market_mood_returns_string(self):
        stock = Stock()
        result = stock.get_market_mood()
        assert isinstance(result, str), "Expected get_market_mood to return a string"

    def test_get_market_mood_non_empty(self):
        stock = Stock()
        result = stock.get_market_mood()
        assert result, "Expected get_market_mood to return a non-empty result"
        
    # testing invalid symbol token when called with get_earnings
    def test_get_earnings_invalid_symbol(self, capsys, monkeypatch):
        test_symbol = 'INVALID_SYMBOL'
        def mock_get(url):
            return MockResponse(200)
        
        monkeypatch.setattr("requests.get", mock_get)
        
        stock = Stock()
        result = stock.get_earnings(test_symbol)
        
        assert result is None, "Expected None when an invalid symbol is provided."
        
        captured = capsys.readouterr()
        assert f"Error: No data found for symbol '{test_symbol}'. Please check if the symbol is correct." in captured.out, "Expected appropriate error message printed."
        

    ## forecast price ##
    # Test1: Forecast Prices Function Returns a DataFrame with the Correct Structure
    def test_forecast_prices_structure(self, monkeypatch):
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
   
    # Test2: Correct Number of Forecasted Days
    def test_forecast_prices_row_count(self, monkeypatch):
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

    # Test3: Predicted Price Range
    def test_forecast_prices_value_range(self, monkeypatch):
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

    ## company_overview ##
    # Test 1: No symbol provided
    def test_company_overview_no_symbol(self, capsys):
        stock = Stock()
        result = stock.company_overview("")
        assert result is None, "Expected None when no symbol is provided."
        captured = capsys.readouterr()
        assert "Error: No symbol provided." in captured.out, "Expected appropriate error message printed."

    # Test 2: Invalid symbol (symbol with no data)
    def test_company_overview_invalid_symbol(self,capsys,monkeypatch):
        test_symbol = 'INVALID_SYMBOL'
        def mock_get(url):
            return MockResponse(200)
        
        monkeypatch.setattr("requests.get", mock_get)
        
        stock = Stock()
        result = stock.company_overview(test_symbol)
        
        assert result is None, "Expected None when an invalid symbol is provided."
        
        captured = capsys.readouterr()
        assert f"Error: No data found for symbol '{test_symbol}'. Please check if the symbol is correct." in captured.out, "Expected appropriate error message printed."

    # Test 3: Valid symbol with successful response
    def test_company_overview_valid_symbol(self,monkeypatch):
        test_symbol = "AAPL"
        SAMPLE_OVERVIEW_JSON = {
                        "Symbol": "AAPL",
                        "Name": "Apple Inc.",
                        "Description": "Apple designs and sells electronics and software.",
                        "CIK": "51140",
                        "Country": "USA",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics"
                    }
        def mock_get(url):
            return MockResponse(200, SAMPLE_OVERVIEW_JSON)

        monkeypatch.setattr("requests.get", mock_get)
        
        # Mock random.choice
        monkeypatch.setattr("random.choice", lambda _: "Invest in {stock}? Fam, that’s more sus than Freddy Fazbear at 3 AM 💀💀💀.")
        
        stock = Stock()
        result = stock.company_overview(test_symbol)
        
        assert isinstance(result, BrainrotWrapper), "Expected BrainrotWrapper object."
        assert result.quote == f"Invest in {test_symbol}? Fam, that’s more sus than Freddy Fazbear at 3 AM 💀💀💀.", "Brainrot quote did not match."
        assert isinstance(result.object, Company), "Expected a Company object in BrainrotWrapper."
        assert result.object.symbol == SAMPLE_OVERVIEW_JSON["Symbol"]
        assert result.object.name == SAMPLE_OVERVIEW_JSON["Name"]
        assert result.object.description == SAMPLE_OVERVIEW_JSON["Description"]
        assert result.object.CIK == SAMPLE_OVERVIEW_JSON["CIK"]
        assert result.object.country == SAMPLE_OVERVIEW_JSON["Country"]
        assert result.object.sector == SAMPLE_OVERVIEW_JSON["Sector"]
        assert result.object.industry == SAMPLE_OVERVIEW_JSON["Industry"]
    
    # Tests for plot_top_movers

    def test_plot_top_movers_no_data(self, monkeypatch):
        """
        Test plot_top_movers with symbols that have no data to ensure it handles empty data gracefully.
        """
        stock = Stock()
        
        # Mock get_price_data to return an empty DataFrame
        def mock_get_price_data(symbol):
            return BrainrotDataFrame("", pd.DataFrame(columns=['date', 'price']))
        
        monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)
        
        result = stock.plot_top_movers(["AAPL", "GOOGL"])
        assert result == "No data available for the provided symbols.", "Expected message for no data available."

    def test_plot_top_movers_single_stock(self, monkeypatch):
        """
        Test plot_top_movers with a single stock symbol to ensure it returns the same stock as both gainer and loser.
        """
        stock = Stock()

        # Mock get_price_data to return mock data for a single stock
        def mock_get_price_data(symbol):
            mock_data = pd.DataFrame({
                'date': pd.date_range(start="2023-01-01", periods=5, freq="D"),
                'price': [100.0, 101.0, 102.0, 103.0, 104.0]  # Increasing prices
            })
            return BrainrotDataFrame("Mock data", mock_data)
        
        monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)
        
        result = stock.plot_top_movers(["AAPL"])
        assert "Top Gainer" in result.df.columns, "Expected Top Gainer column in result."
        assert "Top Loser" in result.df.columns, "Expected Top Loser column in result."
        assert result.df["Top Gainer"]["Symbol"] == "AAPL", "Expected AAPL as top gainer."
        assert result.df["Top Loser"]["Symbol"] == "AAPL", "Expected AAPL as top loser."

    def test_plot_top_movers_multiple_stocks(self, monkeypatch):
        """
        Test plot_top_movers with multiple stock symbols and varying prices to ensure correct top gainer and loser are identified.
        """
        stock = Stock()

        # Mock get_price_data to return different mock data for multiple stocks
        def mock_get_price_data(symbol):
            if symbol == "AAPL":
                mock_data = pd.DataFrame({
                    'date': pd.date_range(start="2023-01-01", periods=5, freq="D"),
                    'price': [100.0, 105.0, 110.0, 115.0, 120.0]  # Increasing prices
                })
            else:
                mock_data = pd.DataFrame({
                    'date': pd.date_range(start="2023-01-01", periods=5, freq="D"),
                    'price': [100.0, 95.0, 90.0, 85.0, 80.0]  # Decreasing prices
                })
            return BrainrotDataFrame("Mock data", mock_data)

        monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)

        result = stock.plot_top_movers(["AAPL", "GOOGL"])
        assert result.df["Top Gainer"]["Symbol"] == "AAPL", "Expected AAPL as top gainer."
        assert result.df["Top Loser"]["Symbol"] == "GOOGL", "Expected GOOGL as top loser."

    # tests for project_future_estimates

    def test_project_future_estimates_no_symbols(self):
        """
        Test project_future_estimates with an empty list to ensure it handles no symbols gracefully.
        """
        stock = Stock()
        result = stock.project_future_estimates([], days=5, pattern="neutral")
        assert result.df.empty, "Expected empty DataFrame when no symbols are provided."


    def test_project_future_estimates_bullish_pattern(self, monkeypatch):
        """
        Test project_future_estimates with a bullish pattern to verify prices trend upward.
        """
        stock = Stock()

        # Mock forecast_prices to return predictable data
        def mock_forecast_prices(symbol, days):
            mock_forecast_data = pd.DataFrame({
                'date': pd.date_range(start="2023-01-10", periods=days, freq="D"),
                'predicted_price': [100.0 for _ in range(days)]
            })
            return BrainrotDataFrame(f"Mock forecast for {symbol}", mock_forecast_data)

        monkeypatch.setattr(stock, "forecast_prices", mock_forecast_prices)

        result = stock.project_future_estimates(["AAPL"], days=5, pattern="bullish")
        assert all(result.df['predicted_price'].diff().dropna() > 0), "Expected bullish trend with increasing prices."


    def test_project_future_estimates_bearish_pattern(self, monkeypatch):
        """
        Test project_future_estimates with a bearish pattern to verify prices trend downward.
        """
        stock = Stock()

        # Mock forecast_prices to return predictable data
        def mock_forecast_prices(symbol, days):
            mock_forecast_data = pd.DataFrame({
                'date': pd.date_range(start="2023-01-10", periods=days, freq="D"),
                'predicted_price': [100.0 for _ in range(days)]
            })
            return BrainrotDataFrame(f"Mock forecast for {symbol}", mock_forecast_data)

        monkeypatch.setattr(stock, "forecast_prices", mock_forecast_prices)

        result = stock.project_future_estimates(["AAPL"], days=5, pattern="bearish")
        assert all(result.df['predicted_price'].diff().dropna() < 0), "Expected bearish trend with decreasing prices."


    def test_project_future_estimates_neutral_pattern(self, monkeypatch):
        """
        Test project_future_estimates with a neutral pattern to verify prices fluctuate slightly.
        """
        stock = Stock()

        # Mock forecast_prices to return predictable data
        def mock_forecast_prices(symbol, days):
            mock_forecast_data = pd.DataFrame({
                'date': pd.date_range(start="2023-01-10", periods=days, freq="D"),
                'predicted_price': [100.0 for _ in range(days)]
            })
            return BrainrotDataFrame(f"Mock forecast for {symbol}", mock_forecast_data)

        monkeypatch.setattr(stock, "forecast_prices", mock_forecast_prices)

        result = stock.project_future_estimates(["AAPL"], days=5, pattern="neutral")
        # Check that prices fluctuate within a range, close to 100 in this case
        price_fluctuations = result.df['predicted_price'].diff().dropna().abs()
        assert all(price_fluctuations < 2), "Expected neutral trend with minor fluctuations."

    @pytest.fixture
    def mock_company(self):
        company_data = {
            "Symbol": "AAPL",
            "Name": "Apple Inc.",
            "Description": "Technology company",
            "CIK": "0000320193",
            "Country": "USA",
            "Sector": "Technology",
            "Industry": "Consumer Electronics"
        }
        return Company(company_data)
    
    def test_forecast_linear_model_last_month(self, mock_company):
        """
        Test forecast with a linear model and last month's data.
        """
        result = mock_company.forecast_by_date_range(date_range="last_month", days_to_forecast=5, model_type="linear")
        
        # Check that the result is a BrainrotDataFrame
        assert isinstance(result, BrainrotDataFrame), "Expected result to be a BrainrotDataFrame."
        
        # Ensure a brainrot quote is present
        assert result.quote, "Expected a brainrot quote to be present."
        
        # Verify forecast DataFrame structure
        assert "predicted_price" in result.df.columns, "Expected 'predicted_price' column in forecast DataFrame."
        assert len(result.df) == 5, "Expected 5 forecasted days."


    def test_forecast_random_walk_model_last_year(self, mock_company):
        """
        Test forecast with a random walk model over last year's data.
        """
        result = mock_company.forecast_by_date_range(date_range="last_year", days_to_forecast=10, model_type="random_walk")
        
        # Check that the result is a BrainrotDataFrame
        assert isinstance(result, BrainrotDataFrame), "Expected result to be a BrainrotDataFrame."
        
        # Ensure a brainrot quote is present
        assert result.quote, "Expected a brainrot quote to be present."
        
        # Verify forecast DataFrame structure
        assert "predicted_price" in result.df.columns, "Expected 'predicted_price' column in forecast DataFrame."
        assert len(result.df) == 10, "Expected 10 forecasted days."
    
    def test_forecast_with_confidence_interval(self, mock_company):
        """
        Test forecast output with confidence interval for a linear model.
        """
        result = mock_company.forecast_by_date_range(
            date_range="last_month", days_to_forecast=5, model_type="linear", confidence_level=0.95
        )
        
        # Check that the result is a BrainrotDataFrame
        assert isinstance(result, BrainrotDataFrame), "Expected result to be a BrainrotDataFrame."
        
        # Verify confidence interval columns exist in the DataFrame
        assert "lower_bound" in result.df.columns, "Expected 'lower_bound' column in forecast DataFrame."
        assert "upper_bound" in result.df.columns, "Expected 'upper_bound' column in forecast DataFrame."
        
        # Ensure that lower bound is less than or equal to predicted price and upper bound is greater
        for _, row in result.df.iterrows():
            assert row["lower_bound"] <= row["predicted_price"], "Lower bound should be less than or equal to predicted price."
            assert row["upper_bound"] >= row["predicted_price"], "Upper bound should be greater than or equal to predicted price."


        # Check that the EMA result length matches input data length
        self.assertEqual(len(result_ema), len(self.trade_info), "EMA result length should match input data length")

        # Check that the first value is NaN
        self.assertTrue(pd.isna(result_ema.iloc[0]), "First EMA value should be NaN due to exponential calculation")

    def test_detect_crossover(self):
        print("\nTesting detect_crossover()")

        # Use short and long SMAs for crossover detection
        short_sma = self.stock.calculate_sma(self.trade_info, window=10)
        long_sma = self.stock.calculate_sma(self.trade_info, window=50)
        result_crossover = self.stock.detect_crossover(short_sma, long_sma)

        # Check that crossover result is not empty
        self.assertFalse(result_crossover.empty, "Crossover result should not be empty")

        # Check if crossover Series has the same length as input data
        self.assertEqual(len(result_crossover), len(short_sma), "Crossover result length should match input data length")

        # Check that crossover values are -1, 0, or 1
        self.assertTrue(result_crossover.isin([-1, 0, 1]).all(), "Crossover values should be -1, 0, or 1")

    def test_calculate_rolling_std(self):
        print("\nTesting calculate_rolling_std()")

        # Check that rolling standard deviation function returns non-empty Series
        result_std = self.stock.calculate_rolling_std(self.trade_info, window=20)
        self.assertFalse(result_std.empty, "Rolling standard deviation result should not be empty")

        # Check that the result length matches input data length
        self.assertEqual(len(result_std), len(self.trade_info), "Rolling standard deviation result length should match input data length")

        # Check that the first 19 values are NaN due to window size
        self.assertTrue(result_std[:19].isna().all(), "First 19 values should be NaN due to window size")

    def test_calculate_atr(self):
        print("\nTesting calculate_atr()")

        # Check that ATR function returns a non-empty Series
        result_atr = self.stock.calculate_atr(self.trade_info, window=14)
        self.assertFalse(result_atr.empty, "ATR result should not be empty")

        # Check that the ATR result has the same length as input data
        self.assertEqual(len(result_atr), len(self.trade_info), "ATR result length should match input data length")

        # Check that the first 13 values are NaN due to window size
        self.assertTrue(result_atr[:13].isna().all(), "First 13 values should be NaN due to window size")

    def test_calculate_momentum(self):
        print("\nTesting calculate_momentum()")

        # Check that momentum function returns a non-empty Series
        result_momentum = self.stock.calculate_momentum(self.trade_info, period=10)
        self.assertFalse(result_momentum.empty, "Momentum result should not be empty")

        # Check that the momentum result has the same length as input data
        self.assertEqual(len(result_momentum), len(self.trade_info), "Momentum result length should match input data length")

        # Check that the first 9 values are NaN due to period size
        self.assertTrue(result_momentum[:9].isna().all(), "First 9 values should be NaN due to period size")

    def test_calculate_roc(self):
        print("\nTesting calculate_roc()")

        # Check that ROC function returns a non-empty Series
        result_roc = self.stock.calculate_roc(self.trade_info, period=10)
        self.assertFalse(result_roc.empty, "ROC result should not be empty")

        # Check that the ROC result has the same length as input data
        self.assertEqual(len(result_roc), len(self.trade_info), "ROC result length should match input data length")

        # Check that the first 9 values are NaN due to period size
        self.assertTrue(result_roc[:9].isna().all(), "First 9 values should be NaN due to period size")

    def test_calculate_volume_moving_average(self):
        print("\nTesting calculate_volume_moving_average()")

        # Check that volume moving average function returns a non-empty Series
        result_volume_ma = self.stock.calculate_volume_moving_average(self.trade_info, window=20)
        self.assertFalse(result_volume_ma.empty, "Volume Moving Average result should not be empty")

        # Check that the volume moving average result has the same length as input data
        self.assertEqual(len(result_volume_ma), len(self.trade_info), "Volume Moving Average result length should match input data length")

        # Check that the first 19 values are NaN due to window size
        self.assertTrue(result_volume_ma[:19].isna().all(), "First 19 values should be NaN due to window size")

    def test_calculate_vpt(self):
        print("\nTesting calculate_vpt()")

        # Check that VPT function returns a non-empty Series
        result_vpt = self.stock.calculate_vpt(self.trade_info)
        self.assertFalse(result_vpt.empty, "VPT result should not be empty")

        # Check that the VPT result has the same length as input data
        self.assertEqual(len(result_vpt), len(self.trade_info), "VPT result length should match input data length")

        # Check that the first value is NaN due to pct_change
        self.assertTrue(pd.isna(result_vpt.iloc[0]), "First VPT value should be NaN due to percentage change")

    def test_calculate_bollinger_bands(self):
        print("\nTesting calculate_bollinger_bands()")

        # Calculate Bollinger Bands and check for non-empty result
        result_bollinger = self.stock.calculate_bollinger_bands(self.trade_info, window=20, num_std_dev=2)
        self.assertFalse(result_bollinger.empty, "Bollinger Bands result should not be empty")

        # Check that the Bollinger Bands result has the correct columns
        self.assertListEqual(list(result_bollinger.columns), ['sma', 'upper_band', 'lower_band'], "Bollinger Bands columns do not match expected format")

        # Check that the result has the same length as input data
        self.assertEqual(len(result_bollinger), len(self.trade_info), "Bollinger Bands result length should match input data length")

    def test_calculate_rsi(self):
        print("\nTesting calculate_rsi()")

        # Calculate RSI and check for non-empty result
        result_rsi = self.stock.calculate_rsi(self.trade_info, period=14)
        self.assertFalse(result_rsi.empty, "RSI result should not be empty")

        # Check that the RSI result has the same length as input data
        self.assertEqual(len(result_rsi), len(self.trade_info), "RSI result length should match input data length")

        # Check that RSI values are between 0 and 100
        self.assertTrue(result_rsi.between(0, 100).all(), "RSI values should be between 0 and 100")

    def test_calculate_daily_range(self):
        print("\nTesting calculate_daily_range()")

        # Check that daily range function returns a non-empty Series
        result_daily_range = self.stock.calculate_daily_range(self.trade_info)
        self.assertFalse(result_daily_range.empty, "Daily Range result should not be empty")

        # Check that daily range result has the same length as input data
        self.assertEqual(len(result_daily_range), len(self.trade_info), "Daily Range result length should match input data length")

        # Check that all daily range values are non-negative
        self.assertTrue((result_daily_range >= 0).all(), "Daily range values should be non-negative")

    def test_calculate_cumulative_return(self):
        print("\nTesting calculate_cumulative_return()")

        # Check that cumulative return function returns a valid result
        result_cumulative_return = self.stock.calculate_cumulative_return(self.trade_info)
        self.assertIsNotNone(result_cumulative_return, "Cumulative return should not be None")

        # Check that cumulative return is a numeric value
        self.assertIsInstance(result_cumulative_return, (float, int), "Cumulative return should be a float or int")

    def test_calculate_sharpe_ratio(self):
        print("\nTesting calculate_sharpe_ratio()")

        # Check that Sharpe Ratio function returns a valid result
        result_sharpe_ratio = self.stock.calculate_sharpe_ratio(self.trade_info)
        self.assertIsNotNone(result_sharpe_ratio, "Sharpe Ratio should not be None")

        # Check that Sharpe Ratio is a numeric value
        self.assertIsInstance(result_sharpe_ratio, (float, int), "Sharpe Ratio should be a float or int")

if __name__ == '__main__':
    unittest.main()