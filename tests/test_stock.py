import pytest
import pandas as pd
from src.Financiers.stock import Stock
import unittest
from unittest.mock import patch
import pandas as pd
from io import StringIO

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
    
    def test_Stockprice_getter(self):
        print("\n Testing test_Stockprice_getter() with AAPL")
        stock = Stock()
        trade_info = stock.Stockprice_getter("AAPL")
        
        # Check that the data has the correct columns
        expected_columns = ["timestamp", "open", "high", "low", "close", "volume"]
        self.assertListEqual(list(trade_info.columns), expected_columns, "Columns do not match expected format")

        # Check data is not empty
        self.assertFalse(trade_info.empty, "Data returned is empty")

        # Check calculate_sma
        result_sma = stock.calculate_sma(trade_info, window=20)
        self.assertFalse(result_sma.empty, "SMA result should not be empty for input data")
        
        # Check calculate_ema
        result_ema = stock.calculate_ema(trade_info, span=20)
        self.assertFalse(result_ema.empty, "EMA result should not be empty for input data")
        
        # Check detect_crossover
        result_crossover = stock.detect_crossover(result_sma, result_ema)
        self.assertFalse(result_crossover.empty, "Crossover result should not be empty for input data")
        
        # Check calculate_rolling_std
        result_std = stock.calculate_rolling_std(trade_info, window=20)
        self.assertFalse(result_std.empty, "Rolling standard deviation result should not be empty for input data")
        
        # Check calculate_atr
        result_atr = stock.calculate_atr(trade_info, window=14)
        self.assertFalse(result_atr.empty, "ATR result should not be empty for input data")
        
        # Check calculate_momentum
        result_momentum = stock.calculate_momentum(trade_info, period=10)
        self.assertFalse(result_momentum.empty, "Momentum result should not be empty for input data")
        
        # Check calculate_roc
        result_roc = stock.calculate_roc(trade_info, period=10)
        self.assertFalse(result_roc.empty, "ROC result should not be empty for input data")
        
        # Check calculate_volume_moving_average
        result_volume_ma = stock.calculate_volume_moving_average(trade_info, window=20)
        self.assertFalse(result_volume_ma.empty, "Volume Moving Average result should not be empty for input data")
        
        # Check calculate_vpt
        result_vpt = stock.calculate_vpt(trade_info)
        self.assertFalse(result_vpt.empty, "VPT result should not be empty for input data")
        
        # Check calculate_bollinger_bands
        result_bollinger = stock.calculate_bollinger_bands(trade_info, window=20, num_std_dev=2)
        self.assertFalse(result_bollinger.empty, "Bollinger Bands result should not be empty for input data")
        self.assertListEqual(list(result_bollinger.columns), ['sma', 'upper_band', 'lower_band'], "Bollinger Bands DataFrame columns do not match expected format")
        
        # Check calculate_rsi
        result_rsi = stock.calculate_rsi(trade_info, period=14)
        self.assertFalse(result_rsi.empty, "RSI result should not be empty for input data")
        
        # Check calculate_stochastic_oscillator
        result_stochastic = stock.calculate_stochastic_oscillator(trade_info, period=14)
        self.assertFalse(result_stochastic.empty, "Stochastic Oscillator result should not be empty for input data")
        
        # Check calculate_daily_range
        result_daily_range = stock.calculate_daily_range(trade_info)
        self.assertFalse(result_daily_range.empty, "Daily Range result should not be empty for input data")
        
        # Check detect_doji
        result_doji = stock.detect_doji(trade_info)
        self.assertFalse(result_doji.empty, "Doji detection result should not be empty for input data")
        
        # Check detect_engulfing
        result_engulfing = stock.detect_engulfing(trade_info)
        self.assertFalse(result_engulfing.empty, "Engulfing pattern detection result should not be empty for input data")
        
        # Check calculate_cumulative_return
        result_cumulative_return = stock.calculate_cumulative_return(trade_info)
        self.assertIsNotNone(result_cumulative_return, "Cumulative return result should not be None for input data")
        
        # Check calculate_sharpe_ratio
        result_sharpe_ratio = stock.calculate_sharpe_ratio(trade_info)
        self.assertIsNotNone(result_sharpe_ratio, "Sharpe Ratio result should not be None for input data")



            
            

