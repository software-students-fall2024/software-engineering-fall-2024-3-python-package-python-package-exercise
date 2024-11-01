import pytest
import pandas as pd
from src.Financiers.stock import Stock

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
