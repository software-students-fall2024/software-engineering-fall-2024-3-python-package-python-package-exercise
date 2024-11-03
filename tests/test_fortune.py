import pytest
from unittest.mock import patch, mock_open
from fortunes.send_email import send_fortune_email
from fortunes.random_fortune import get_fortune_cookie

def test_get_fortune_cookie_basic():
    # Mock the content of the fortune.txt file with multiple fortunes
    mock_fortunes = "Fortune 1 % Fortune 2 % Fortune 3"
    
    with patch('fortunes.random_fortune.importlib.resources.open_text', mock_open(read_data=mock_fortunes)):
        with patch('fortunes.random_fortune.random.choice', return_value="Fortune 2"):
            with patch('fortunes.random_fortune.random.randint', return_value=42):
                result = get_fortune_cookie()
                
                # Check if the output matches the expected format
                assert result == "🔮 Your Fortune: Fortune 2\n🍀 Your Lucky Number: 42"

def test_get_fortune_cookie_random_calls():
    mock_fortunes = "Fortune 1 % Fortune 2 % Fortune 3"
    
    with patch('fortunes.random_fortune.importlib.resources.open_text', mock_open(read_data=mock_fortunes)):
        with patch('fortunes.random_fortune.random.choice') as mock_choice, \
             patch('fortunes.random_fortune.random.randint') as mock_randint:
            
            mock_choice.return_value = "Fortune 1"
            mock_randint.return_value = 88
            get_fortune_cookie()
            
            # Ensure random.choice and random.randint were called once each
            mock_choice.assert_called_once()
            mock_randint.assert_called_once()

def test_get_fortune_cookie_empty_file():
    # Test for an empty fortune file
    mock_fortunes = ""
    
    with patch('fortunes.random_fortune.importlib.resources.open_text', mock_open(read_data=mock_fortunes)):
        with pytest.raises(IndexError):  # random.choice will raise IndexError on an empty list
            get_fortune_cookie()

def test_get_fortune_cookie_single_fortune():
    # Test the case where there's only one fortune in the file
    mock_fortunes = "Single fortune only"
    
    with patch('fortunes.random_fortune.importlib.resources.open_text', mock_open(read_data=mock_fortunes)):
        with patch('fortunes.random_fortune.random.choice', return_value="Single fortune only"):
            with patch('fortunes.random_fortune.random.randint', return_value=7):
                result = get_fortune_cookie()
                
                # Ensure it returns the single fortune and a lucky number
                assert result == "🔮 Your Fortune: Single fortune only\n🍀 Your Lucky Number: 7"

def test_get_fortune_cookie_large_fortunes():
    # Test with a large number of fortunes in the file
    mock_fortunes = "Fortune " + " % ".join(str(i) for i in range(1000))
    
    with patch('fortunes.random_fortune.importlib.resources.open_text', mock_open(read_data=mock_fortunes)):
        with patch('fortunes.random_fortune.random.choice', return_value="Fortune 999"):
            with patch('fortunes.random_fortune.random.randint', return_value=99):
                result = get_fortune_cookie()
                
                # Ensure it selects a fortune from the large list
                assert result == "🔮 Your Fortune: Fortune 999\n🍀 Your Lucky Number: 99"

def test_send_fortune_email_single_fortune():
    recipient_email = "test@example.com"
    fortune = "🔮 Your Fortune: Good things are coming your way!\n🍀 Your Lucky Number: 7"

    with patch('fortunes.send_email.smtplib.SMTP') as mock_smtp:
        send_fortune_email(recipient_email, fortune)

        mock_smtp.assert_called_with("smtp.gmail.com", 587)
        instance = mock_smtp.return_value.__enter__.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once()
        instance.sendmail.assert_called_once()

def test_send_fortune_email_multiple_fortunes():
    recipient_email = "test@example.com"
    fortunes = [
        "🔮 Your Fortune: Happiness is around the corner.\n🍀 Your Lucky Number: 12",
        "🔮 Your Fortune: Success is in your future.\n🍀 Your Lucky Number: 24"
    ]

    with patch('fortunes.send_email.smtplib.SMTP') as mock_smtp:
        send_fortune_email(recipient_email, fortunes)

        mock_smtp.assert_called_with("smtp.gmail.com", 587)
        instance = mock_smtp.return_value.__enter__.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once()
        instance.sendmail.assert_called_once()

def test_send_fortune_email_invalid_email():
    recipient_email = "invalid-email"
    fortune = "🔮 Your Fortune: Be cautious today.\n🍀 Your Lucky Number: 13"

    with pytest.raises(Exception):
        send_fortune_email(recipient_email, fortune)

def test_send_fortune_email_server_connection_failure():
    recipient_email = "test@example.com"
    fortune = "🔮 Your Fortune: Good things are coming your way!\n🍀 Your Lucky Number: 7"

    with patch('fortunes.send_email.smtplib.SMTP', side_effect=Exception("Failed to connect")):
        with pytest.raises(Exception, match="Failed to connect"):
            send_fortune_email(recipient_email, fortune)

def test_send_fortune_email_empty_fortune():
    recipient_email = "test@example.com"
    fortune = ""

    with patch('fortunes.send_email.smtplib.SMTP') as mock_smtp:
        send_fortune_email(recipient_email, fortune)

        mock_smtp.assert_called_with("smtp.gmail.com", 587)
        instance = mock_smtp.return_value.__enter__.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once()
        instance.sendmail.assert_called_once()

def test_send_fortune_email_large_fortune():
    recipient_email = "test@example.com"
    fortune = "🔮 " + "Your Fortune is very bright! " * 1000  # Create a very large fortune message

    with patch('fortunes.send_email.smtplib.SMTP') as mock_smtp:
        send_fortune_email(recipient_email, fortune)

        mock_smtp.assert_called_with("smtp.gmail.com", 587)
        instance = mock_smtp.return_value.__enter__.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once()
        instance.sendmail.assert_called_once()

def test_send_fortune_email_with_special_characters():
    recipient_email = "test@example.com"
    fortune = "🔮 Your Fortune: 🎉 Congratulations! 💸 Money is coming your way! 🍀 Lucky Number: 88"

    with patch('fortunes.send_email.smtplib.SMTP') as mock_smtp:
        send_fortune_email(recipient_email, fortune)

        mock_smtp.assert_called_with("smtp.gmail.com", 587)
        instance = mock_smtp.return_value.__enter__.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once()
        instance.sendmail.assert_called_once()
