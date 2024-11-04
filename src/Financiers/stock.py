import pandas as pd
import requests
from dotenv import load_dotenv
import os
import random
from .quotes import quotes

load_dotenv()


class Stock:
    def __init__(self):
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY")

    # TODO: add optional argument for quarterly or annual
    def get_earnings(self, symbol_string, annual=True):
        """
        Retrieves the annual and quarterly earnings (EPS) for the company of interest
        Arguments:
        symbol_string: a string representing the ticker of your choice. For example: symbol=IBM.
        annual: optional bool for whether earnings are reported quarterly or annually. default annual (True)

        Returns:
        a custom pandas DataFrame BrainrotDataFrame containing a random brainrot quote and a DataFrame with two columns 'date' and 'reportedEPS'
        """
        url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol_string}&apikey={self.api_key}"

        response = requests.get(url)
        data = response.json()
        
        if annual == True:
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
