import pytest
import pandas as pd
from src.Financiers.stock import Stock
import unittest
from unittest.mock import patch
import pandas as pd
from io import StringIO
import numpy as np


class TestStockFunctions(unittest.TestCase):

    def setUp(self):
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

if __name__ == '__main__':
    unittest.main()