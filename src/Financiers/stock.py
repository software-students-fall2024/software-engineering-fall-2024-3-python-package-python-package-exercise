import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
class Stock:
    def __init__(self):
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        