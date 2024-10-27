#import pytest
import unittest
from codeshakespeare.shakespeare import to_shakespeare, to_shakespeare_error, get_random_shakespeare_quote, generate_shakespearean_commit_message

class TestCodeShakespeare(unittest.TestCase):

    def test_to_shakespeare_noble(self):
        """Test the 'noble' option of the to_shakespeare function"""
        comment = "This function sorts a list."
        result = to_shakespeare(comment, formality="noble")
        self.assertEqual(result, "// O noble comment, This function sorts a list, thou art rephrased in grandeur!")

    def test_to_shakespeare_courtly(self):
        """Test the 'courtly' option of the to_shakespeare function"""
        comment = "This function filters data."
        result = to_shakespeare(comment, formality="courtly")
        self.assertEqual(result, "// Most esteemed comment, This function filters data, thy wisdom shines like the sun.")

    def test_to_shakespeare_error_tragedy(self):
        """Test the 'tragedy' option of the to_shakespeare_error function"""
        error_msg = "Index out of range."
        result = to_shakespeare_error(error_msg, severity="tragedy")
        self.assertEqual(result, "Alas, an error hath occurred: 'Index out of range'. 'Tis a tragedy most foul.")

    def test_to_shakespeare_error_comedy(self):
        """Test the 'comedy' option of the to_shakespeare_error function"""
        error_msg = "File not found."
        result = to_shakespeare_error(error_msg, severity="comedy")
        self.assertEqual(result, "Fret not, for an error hath occurred: 'File not found'. But we shall laugh in its face!")

    def test_get_random_shakespeare_quote_playful(self):
        """Test the 'playful' option of the get_random_shakespeare_quote function"""
        result = get_random_shakespeare_quote(style="playful")
        playful_quotes = [
            "To code, or not to code, that is the question.",
            "Cry havoc and let slip the bugs of war!",
            "Parting is such sweet sorrow... especially when closing your IDE."
        ]
        self.assertIn(result, playful_quotes)

    def test_generate_shakespearean_commit_message_victory(self):
        """Test the 'victory' option of the generate_shakespearean_commit_message function"""
        result = generate_shakespearean_commit_message(emotion="victory")
        victorious_messages = [
            "Commit thy changes, for they doth bring glory!",
            "Thine errors are slain, and the code is just!",
            "This branch, once barren, now flourisheth with code."
        ]
        self.assertIn(result, victorious_messages)

if __name__ == '__main__':
    unittest.main()