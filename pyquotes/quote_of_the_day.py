import random
import datetime
from .quotes import inspirational, iconic, sad, funny

def get_quote_of_the_day():
    all= inspirational + iconic + sad + funny
    today = datetime.date.today()
    
    random.seed(today.toordinal())
    quote_of_the_day = random.choice(all)
    
    return quote_of_the_day