from io import StringIO
import sys
from src.guessFact.code import hello_world

def test_hello_world_output():
    """Test that hello_world prints 'Hello World!' to the console."""
    captured_output = StringIO()
    sys.stdout = captured_output #redirect stdout to capture print output
    hello_world()
    sys.stdout = sys.__stdout__ #reset stdout
    assert captured_output.getvalue().strip() == "Hello World!"
