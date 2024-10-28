import pytest

from funky_fortune.main import zodiac_fortune, lucky_number, fortune_cookie, magic_8ball

def test_zodiac_fortune():
    assert zodiac_fortune("Aries") in ["You'll meet a talking sheep today", "Watch out for ram horns", "Your wool sweater will bring good luck"]
    assert zodiac_fortune("Taurus") in ["Today is perfect for beef noodles", "You'll find a gold coin", "Don't be as stubborn as a bull"]

# test if there is no assigned zodiac, it will return default response
def test_zodiac_fortune_special_sign():
    assert zodiac_fortune("UnknownZodiac") == "Your zodiac sign is too special, I can't predict it"






def test_lucky_number():
    
    assert 0 <= lucky_number("RandomName") < 100

# make sure same name return same lucky number
def test_lucky_number_consistency():
    assert lucky_number("sameName") == lucky_number("sameName")

# make sure special character also return valid lucky number
def test_lucky_number_edge_cases():
    assert lucky_number("") == 0
    assert 0 <= lucky_number("123!@#") < 100

def test_fortune_cookie():
    assert fortune_cookie() in ["You'll be very lucky today", "Slow and steady wins the race", "Today is perfect for trying new things", "Remember to call your family"]
    assert fortune_cookie(lucky=True).startswith("Extra lucky: ")
    for _ in range(100):
        assert fortune_cookie().startswith("Extra lucky: ") == False

# make sure the return results are random
def test_fortune_cookie_randomness():
    results = {fortune_cookie() for _ in range(10)}
    assert len(results)>1

def test_magic_8ball():
    question = "Will I become rich today?"
    answer = magic_8ball(question)
    assert question in answer
    assert any(response in answer for response in ["It is certain", "It is decidedly so", "Without a doubt", "You may rely on it", "My reply is no", "Better not tell you now", "Outlook not so good", "Cannot predict now"])
