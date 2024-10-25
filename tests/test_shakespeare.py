import pytest
from codeshakespeare.shakespeare import (
    to_shakespeare, to_shakespeare_error, 
    get_random_shakespeare_quote, generate_shakespearean_commit_message
)

def test_to_shakespeare():
    assert to_shakespeare("Fix the bug") == "// O noble comment, Fix the bug, thou art rephrased in grandeur!"

def test_to_shakespeare_error():
    assert to_shakespeare_error("IndexError") == "Alas, an error hath occurred: 'IndexError'. 'Tis a tragedy most foul."

def test_get_random_shakespeare_quote():
    quote = get_random_shakespeare_quote()
    assert quote in [
        "To code, or not to code, that is the question.",
        "Cry havoc and let slip the bugs of war!",
        "Parting is such sweet sorrow... especially when closing your IDE."
    ]

def test_generate_shakespearean_commit_message():
    commit_message = generate_shakespearean_commit_message()
    assert commit_message in [
        "Commit thy changes, for they doth bring glory!",
        "This branch, once barren, now flourisheth with code.",
        "Thine errors are slain, and the code is just!"
    ]
