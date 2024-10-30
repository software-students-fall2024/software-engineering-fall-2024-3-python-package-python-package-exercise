import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
class Stock:
    def __init__(self):
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        
    def get_earnings(self, symbol_string):
        url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol_string}&apikey={self.api_key}'
        
        response = requests.get(url)
        data = response.json()
        
        annualEarnings = pd.DataFrame(data['annualEarnings']) # convert 'annualEarnings' from json (list of dictionaries orignally) into DataFrame
        annualEarnings = annualEarnings[['fiscalDateEnding', 'reportedEPS']] # select only two columns, fiscalDateEnding and reportedEPS from annualEarnings df
        annualEarnings.columns = ['date', 'reportedEPS'] # rename the columns for beter readability
        annualEarnings['type'] = 'Annual' # added this to differentiate between quarterly earnings below vvvv

        # and just do the same thing above for below for quarterly earnings cuz the API call happens to return both
        quarterlyEarnings = pd.DataFrame(data['quarterlyEarnings']) 
        quarterlyEarnings = quarterlyEarnings[['fiscalDateEnding', 'reportedEPS']]
        quarterlyEarnings.columns = ['date', 'reportedEPS']
        quarterlyEarnings['type'] = 'Quarterly'
        
        earnings_df = pd.concat([annualEarnings, quarterlyEarnings], ignore_index=True) # concat (combine) annual and quarterly earnings into a single df (dataframe)
        
        earnings_df = earnings_df.sort_values(by='date', ascending=False).reset_index(drop=True) # sort df by date (otherwise it wasn't sorted)
        
        return earnings_df
