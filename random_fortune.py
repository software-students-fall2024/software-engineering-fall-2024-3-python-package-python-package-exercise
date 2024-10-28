"""
this function will return you a random fortune cookie quote and a random lucky number
have fun!
"""

import random
def get_fortune_cookie():
    #load the quotes from file
    with open ('.../resource/fortune.txt','r')as file:
        content = file.read()
        fortunes = [quote.strip() for quote in content.split ('%') if quote.strip()]

    fortune = random.choice (fortunes)
    lucky_num  = random.randint(0,99)
    #print the fortune and number to user
    print(f"🔮 Your Fortune: {fortune}\n🍀 Your Lucky Number: {lucky_num}")

    return fortune, lucky_num