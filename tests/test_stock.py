import pytest
import pandas as pd
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

class Tests:
    
    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        From the main project directory, run the `python -m pytest -s` command to run all tests with print statements (-s) if u include them
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be True!"
        
    
    def test_get_earnings(self, monkeypatch):
        mock_earnings_data = {
            "symbol": "IBM",
            "annualEarnings": [
                {"fiscalDateEnding": "2022-12-31", "reportedEPS": "12.34"},
                {"fiscalDateEnding": "2021-12-31", "reportedEPS": "10.12"}
            ],
            "quarterlyEarnings": [
                {"fiscalDateEnding": "2022-12-31", "reportedEPS": "3.21"},
                {"fiscalDateEnding": "2022-09-30", "reportedEPS": "2.98"}
            ]
        }

        def mock_get(*args, **kwargs):
            return MockResponse(200, mock_earnings_data)

        monkeypatch.setattr("requests.get", mock_get)
        
        stock = Stock()
        earnings = stock.get_earnings("IBM")
        
        # check that the response has the correct columns
        expected_columns = ['date', 'reportedEPS']
        assert list(earnings.df.columns) == expected_columns, "DataFrame columns do not match expected columns"
        
        # check that the brainrot dataframe is not empty
        assert not earnings.df.empty, "Earnings DataFrame is empty, but it was expected to contain data"
        
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
        
    def test_get_earnings_numDays(self):
        stock = Stock()

        # test with numDays=None (should return all available entries)
        earnings_all = stock.get_earnings("IBM", annual=True, numDays=None)
        assert earnings_all is not None, "Expected a BrainrotDataFrame to be returned but got None"
        total_rows = len(earnings_all.df)
        assert total_rows > 0, "Expected earnings data to have entries"

        # test with specific numDays as 5
        test_numDays = 5
        earnings_limited = stock.get_earnings("IBM", annual=True, numDays=test_numDays)
        assert earnings_limited is not None, "Expected a BrainrotDataFrame to be returned but got None"
        assert len(earnings_limited.df) == test_numDays, f"Expected {test_numDays} rows, got {len(earnings_limited.df)}"

        # Verify that rows in the limited output are a subset of the full dataset
        assert earnings_limited.df.equals(earnings_all.df.head(test_numDays)), "Expected the limited rows to match the most recent rows"
            
            

    # def test_forecast_prices(self, monkeypatch):
    #     print("\nTesting forecast_prices() with mock data")

    #     # Mock get_price_data to return sample historical data
    #     def mock_get_price_data(symbol_string):
    #         mock_price_data = pd.DataFrame({
    #             'date': pd.date_range(start="2023-01-01", periods=10, freq="D"),
    #             'price': [100.0 + i for i in range(10)]  # increasing mock prices
    #         })
    #         return BrainrotDataFrame("Mock data", mock_price_data)
        
    #     # Apply monkeypatch to replace get_price_data method
    #     stock = Stock()
    #     monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)

    #     # Act: Call the forecast_prices function
    #     days_to_forecast = 5
    #     forecast = stock.forecast_prices("IBM", days=days_to_forecast)

    #     # Assert: Check if the returned BrainrotDataFrame has expected structure
    #     assert forecast.df is not None, "Forecast DataFrame should not be None"
    #     assert 'date' in forecast.df.columns, "'date' column missing from forecast DataFrame"
    #     assert 'predicted_price' in forecast.df.columns, "'predicted_price' column missing from forecast DataFrame"
        
    #     # Check if the correct number of forecasted rows is generated
    #     assert len(forecast.df) == days_to_forecast, f"Expected {days_to_forecast} rows in forecast DataFrame, but got {len(forecast.df)}"
        
    #     # Validate that forecasted dates start the day after the latest historical date
    #     expected_start_date = mock_get_price_data("IBM").df['date'].max() + timedelta(days=1)
    #     actual_start_date = forecast.df['date'].min()
    #     assert actual_start_date == expected_start_date, f"Expected start date {expected_start_date}, but got {actual_start_date}"

    #     # Verify that all predicted prices are within the mocked range (100, 150)
    #     assert forecast.df['predicted_price'].between(100, 150).all(), "Predicted prices are not within the expected range (100, 150)"
        
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
    
    # Tests for get_top_movers

    def test_get_top_movers_no_data(self, monkeypatch):
        """
        Test get_top_movers with symbols that have no data to ensure it handles empty data gracefully.
        """
        stock = Stock()
        
        # Mock get_price_data to return an empty DataFrame
        def mock_get_price_data(symbol):
            return BrainrotDataFrame("", pd.DataFrame(columns=['date', 'price']))
        
        monkeypatch.setattr(stock, "get_price_data", mock_get_price_data)
        
        result = stock.get_top_movers(["AAPL", "GOOGL"])
        assert result == "No data available for the provided symbols.", "Expected message for no data available."

    def test_get_top_movers_single_stock(self, monkeypatch):
        """
        Test get_top_movers with a single stock symbol to ensure it returns the same stock as both gainer and loser.
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
        
        result = stock.get_top_movers(["AAPL"])
        assert "Top Gainer" in result.df.columns, "Expected Top Gainer column in result."
        assert "Top Loser" in result.df.columns, "Expected Top Loser column in result."
        assert result.df["Top Gainer"]["Symbol"] == "AAPL", "Expected AAPL as top gainer."
        assert result.df["Top Loser"]["Symbol"] == "AAPL", "Expected AAPL as top loser."

    def test_get_top_movers_multiple_stocks(self, monkeypatch):
        """
        Test get_top_movers with multiple stock symbols and varying prices to ensure correct top gainer and loser are identified.
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

        result = stock.get_top_movers(["AAPL", "GOOGL"])
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
