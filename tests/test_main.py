import pytest
from funky_fortune.main import zodiac_fortune, lucky_number, fortune_cookie, magic_8ball

def test_zodiac_fortune():
    assert zodiac_fortune("Aries") in ["You'll meet a talking sheep today", "Watch out for ram horns", "Your wool sweater will bring good luck"]
    assert zodiac_fortune("Taurus") in ["Today is perfect for beef noodles", "You'll find a gold coin", "Don't be as stubborn as a bull"]
    assert zodiac_fortune("Unknown") == ["Your zodiac sign is too special, I can't predict it"]

def test_lucky_number():
    assert lucky_number("John") == 74
    assert lucky_number("Alice") == 90
    assert 0 <= lucky_number("RandomName") < 100

def test_fortune_cookie():
    assert fortune_cookie() in ["You'll be very lucky today", "Slow and steady wins the race", "Today is perfect for trying new things", "Remember to call your family"]
    assert fortune_cookie(lucky=True).startswith("Extra lucky: ")
    assert len([x for x in [fortune_cookie() for _ in range(100)] if x.startswith("Extra lucky")]) == 0

def test_magic_8ball():
    question = "Will I become rich today?"
    answer = magic_8ball(question)
    assert question in answer
    assert any(response in answer for response in ["It is certain", "It is decidedly so", "Without a doubt", "You may rely on it", "My reply is no", "Better not tell you now", "Outlook not so good", "Cannot predict now"])
