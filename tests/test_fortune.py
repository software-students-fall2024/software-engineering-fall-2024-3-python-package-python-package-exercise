import pytest
from unittest.mock import patch, MagicMock
from fortunes.send_email import send_fortune_email

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
