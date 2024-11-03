from .getMultipleFortunes import getMultipleFortunes
from .get_quotes_by_author import parse_fortune_file, get_quotes_by_author
from .random_fortune import get_fortune_cookie
from .send_email import send_fortune_email

__all__ = [
    "getMultipleFortunes",
    "parse_fortune_file",
    "get_quotes_by_author",
    "get_fortune_cookie",
    "send_fortune_email"
]