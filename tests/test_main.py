import pytest

from funky_fortune.main import zodiac_fortune, lucky_number, fortune_cookie, magic_8ball

def test_zodiac_fortune():
    assert zodiac_fortune("Aries") in ["You'll meet a talking sheep today", "Watch out for ram horns", "Your wool sweater will bring good luck"]
    assert zodiac_fortune("Taurus") in ["Today is perfect for beef noodles", "You'll find a gold coin", "Don't be as stubborn as a bull"]

# test if there is no assigned zodiac, it will return default response
def test_zodiac_fortune_special_sign():
    assert zodiac_fortune("UnknownZodiac") == "Your zodiac sign is too special, I can't predict it"

# Additional zodiac tests
def test_zodiac_fortune_case_sensitivity():
    # Test case insensitivity
    assert zodiac_fortune("ARIES") == "Your zodiac sign is too special, I can't predict it"
    assert zodiac_fortune("aries") == "Your zodiac sign is too special, I can't predict it"

def test_zodiac_fortune_all_signs():
    # Test all zodiac signs return valid fortunes
    all_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    for sign in all_signs:
        fortune = zodiac_fortune(sign)
        assert isinstance(fortune, str)
        assert len(fortune) > 0

def test_zodiac_fortune_invalid_inputs():
    # Test various invalid inputs
    invalid_inputs = ["", " ", "123", None, "NotASign"]
    for invalid_input in invalid_inputs:
        assert zodiac_fortune(invalid_input) == "Your zodiac sign is too special, I can't predict it"

def test_lucky_number():
    assert 0 <= lucky_number("RandomName") < 100

# make sure same name return same lucky number
def test_lucky_number_consistency():
    assert lucky_number("sameName") == lucky_number("sameName")

# make sure special character also return valid lucky number
def test_lucky_number_edge_cases():
    assert lucky_number("") == 0
    assert 0 <= lucky_number("123!@#") < 100

# Additional lucky number tests
def test_lucky_number_range():
    # Test with various length inputs
    test_cases = [
        "A" * 1000,  # Very long name
        "Hello World!",  # With spaces and punctuation
        "12345",  # Only numbers
        "测试",  # Unicode characters
        "    ",  # Only spaces
    ]
    for test_case in test_cases:
        result = lucky_number(test_case)
        assert isinstance(result, int)
        assert 0 <= result < 100

def test_lucky_number_special_chars():
    # Test with special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    result = lucky_number(special_chars)
    assert isinstance(result, int)
    assert 0 <= result < 100

def test_fortune_cookie():
    assert fortune_cookie() in ["You'll be very lucky today", "Slow and steady wins the race", "Today is perfect for trying new things", "Remember to call your family"]
    assert fortune_cookie(lucky=True).startswith("Extra lucky: ")
    for _ in range(100):
        assert fortune_cookie().startswith("Extra lucky: ") == False

# Additional fortune cookie tests
def test_fortune_cookie_lucky_consistency():
    # Test that lucky prefix is consistent
    for _ in range(50):
        fortune = fortune_cookie(lucky=True)
        assert fortune.startswith("Extra lucky: ")
        assert len(fortune) > 12  # "Extra lucky: " is 12 chars

def test_fortune_cookie_distribution():
    # Test that all possible fortunes appear
    all_fortunes = set()
    for _ in range(100):
        all_fortunes.add(fortune_cookie())
    assert len(all_fortunes) >= 4  # Should have at least 4 different fortunes

def test_magic_8ball():
    question = "Will I become rich today?"
    answer = magic_8ball(question)
    assert question in answer
    assert any(response in answer for response in ["It is certain", "It is decidedly so", "Without a doubt", "You may rely on it", "My reply is no", "Better not tell you now", "Outlook not so good", "Cannot predict now"])

# Additional magic 8ball tests
def test_magic_8ball_empty_question():
    # Test with empty question
    result = magic_8ball("")
    assert result.startswith("Question: ")
    assert "\nAnswer: " in result

def test_magic_8ball_long_question():
    # Test with a very long question
    long_question = "Why " * 100
    result = magic_8ball(long_question)
    assert result.startswith("Question: ")
    assert "\nAnswer: " in result

def test_magic_8ball_special_chars():
    # Test with special characters
    special_question = "Will I win $1,000,000 tomorrow?!?!?"
    result = magic_8ball(special_question)
    assert special_question in result
    assert "\nAnswer: " in result

def test_magic_8ball_response_distribution():
    # Test that we get different responses
    responses = set()
    for _ in range(100):
        result = magic_8ball("Test question")
        response = result.split("\nAnswer: ")[1]
        responses.add(response)
    assert len(responses) > 4  # Should get multiple different responses

# Test combinations of functions
def test_combined_functionality():
    # Test using multiple functions together
    name = "TestUser"
    lucky_num = lucky_number(name)
    zodiac = "Aries"
    
    # Test that lucky number affects fortune cookie
    assert isinstance(lucky_num, int)
    assert isinstance(zodiac_fortune(zodiac), str)
    assert isinstance(fortune_cookie(lucky=(lucky_num > 50)), str)
