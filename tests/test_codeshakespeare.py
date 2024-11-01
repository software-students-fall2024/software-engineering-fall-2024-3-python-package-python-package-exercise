import pytest
import unittest
from codeshakespeare.shakespeare import to_shakespeare, to_shakespeare_error, get_random_shakespeare_quote, generate_shakespearean_commit_message

class TestCodeShakespeare(unittest.TestCase):
    
    # Test "noble" option of to_shakespeare()
    def test_to_shakespeare_noble(self):
        comment = "This function sorts a list."
        result = to_shakespeare(comment, formality="noble")
        self.assertEqual(result, "// O noble comment, This function sorts a list, thou art rephrased in grandeur!")

    # Test "courtly" option of to_shakespeare()
    def test_to_shakespeare_courtly(self):
        comment = "This function filters data."
        result = to_shakespeare(comment, formality="courtly")
        self.assertEqual(result, "// Most esteemed comment, This function filters data, thy wisdom shines like the sun.")

    # Test "tragedy" option of to_shakespeare_error()
    def test_to_shakespeare_error_tragedy(self):
        error_msg = "Index out of range."
        result = to_shakespeare_error(error_msg, severity="tragedy")
        self.assertEqual(result, "Alas, an error hath occurred: 'Index out of range'. 'Tis a tragedy most foul.")

    # Test "comedy" option of to_shakespeare_error()
    def test_to_shakespeare_error_comedy(self):
        error_msg = "File not found."
        result = to_shakespeare_error(error_msg, severity="comedy")
        self.assertEqual(result, "Fret not, for an error hath occurred: 'File not found'. But we shall laugh in its face!")

    # Test "playful" option of get_random_shakespeare_quote()
    def test_get_random_shakespeare_quote_playful(self):
        result = get_random_shakespeare_quote(style="playful")
        playful_quotes = [
            "To code, or not to code, that is the question.",
            "Cry havoc and let slip the bugs of war!",
            "Parting is such sweet sorrow... especially when closing your IDE.",
            "There live not three good men unhanged in England: and one of them is fat.",
            "Mine eyes smell onions.",
            "It is like a barber’s chair that fits all buttocks, the pin-buttock, the quatch-buttock, the brawn-buttock, or any buttock."
        ]
        self.assertIn(result, playful_quotes)

    # Test "victory" option of generate_shakespeare_commit_message()
    def test_generate_shakespearean_commit_message_victory(self):
        result = generate_shakespearean_commit_message(emotion="victory")
        victorious_messages = [
            "Commit thy changes, for they doth bring glory!",
            "Thine errors are slain, and the code is just!",
            "This branch, once barren, now flourisheth with code.",
            "Then with the losers let it sympathize, For nothing can seem foul to those that win.",
            "Sound trumpets! Let our bloody colours wave! And either victory, or else a grave."
            "A victory is twice itself when the achiever brings home full numbers."
        ]
        self.assertIn(result, victorious_messages)

# Main code
if __name__ == '__main__':
    unittest.main()
