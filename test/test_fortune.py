<<<<<<< HEAD
# tests/test_send_fortune_email.py
import pytest
from unittest.mock import patch, MagicMock
from fortune_package.email_utils import send_fortune_email

@patch('fortune_package.email_utils.smtplib.SMTP')
def test_send_fortune_email_single_fortune(mock_smtp):
    recipient_email = "test@example.com"
    fortune = "🔮 Your Fortune: Good things are coming your way!\n🍀 Your Lucky Number: 7"

    send_fortune_email(recipient_email, fortune)

    assert mock_smtp.called, "SMTP server should be called"
    instance = mock_smtp.return_value.__enter__.return_value
    assert instance.sendmail.called, "sendmail should be called"

@patch('fortune_package.email_utils.smtplib.SMTP')
def test_send_fortune_email_multiple_fortunes(mock_smtp):
    recipient_email = "test@example.com"
    fortunes = [
        "🔮 Your Fortune: Happiness is around the corner.\n🍀 Your Lucky Number: 12",
        "🔮 Your Fortune: Success is in your future.\n🍀 Your Lucky Number: 24"
    ]

    send_fortune_email(recipient_email, fortunes)

    assert mock_smtp.called, "SMTP server should be called"
    instance = mock_smtp.return_value.__enter__.return_value
    assert instance.sendmail.called, "sendmail should be called"

def test_send_fortune_email_invalid_email():
    recipient_email = "invalid-email"
    fortune = "🔮 Your Fortune: Be cautious today.\n🍀 Your Lucky Number: 13"

    with pytest.raises(Exception):
        send_fortune_email(recipient_email, fortune)
=======
import pytest
from unittest.mock import patch

<<<<<<< HEAD
=======
from src.fortune import send_email
>>>>>>> adddedd968dbe83bc6782f06abc01a180f5a7c2b
>>>>>>> 8c6c3d31ad7c841b9a1c0555cfae4c62e93df3a0
