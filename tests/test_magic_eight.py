import unittest

from src.magic_eight.magic_eight import get_answers, get_questions, ask_question, shake_ball

class TestMagicEight(unittest.TestCase):
## testing get_answers
    def test_get_answers_just_language(self):
        """Test the get_answers function with just language input"""
        expected = [
            "Don't count on it",
            "Yes",
            "No",
            "Maybe",
            "Ask again later",
            "I doubt it",
            "Certainly",
            "I don't know"
        ]
        result = get_answers("en")
        self.assertEqual(result, expected)

    def test_get_answers_language_and_valid_count(self):
        """Test the get_answers function with language and count input"""
        expected = [
            "Don't count on it",
            "Yes",
            "No"
        ]
        result = get_answers("en", 3)
        self.assertEqual(result, expected)

    def test_get_answers_language_and_invalid_count(self):
        """Test the get_answers function with language and count input beyond size of answers[]"""
        expected = [
            "Don't count on it",
            "Yes",
            "No",
            "Maybe",
            "Ask again later",
            "I doubt it",
            "Certainly",
            "I don't know"
        ]
        result = get_answers("en",-3)
        self.assertEqual(result, expected)
        
## testing get_questions
    def test_get_questions_just_language(self):
        """Test the get_questions function with just language input"""
        expected = [
            "Will I pass this class",
            "Will tomorrow be a snow day",
            "Will I get the internship"
        ]
        result = get_questions("en")
        self.assertEqual(result, expected)

    def test_get_questions_language_and_valid_count(self):
        """Test the get_questions function with language and count input"""
        expected = [
            "Will I pass this class"
        ]
        result = get_questions("en", 1)
        self.assertEqual(result, expected)

    def test_get_questions_language_and_invalid_count(self):
        """Test the get_questions function with language and count input beyond size of questions[]"""
        expected = [
            "Will I pass this class",
            "Will tomorrow be a snow day",
            "Will I get the internship"
        ]
        result = get_questions("en",4)
        self.assertEqual(result, expected)

## testing ask_question
    def test_ask_question_specific(self):
        """Test ask_question with a specific question"""
        question, answer = ask_question("en", "Will I pass this class")
        expected_question = "Will I pass this class"
        expected = [
            "Don't count on it",
            "Yes",
            "No",
            "Maybe",
            "Ask again later",
            "I doubt it",
            "Certainly",
            "I don't know"
        ]
        self.assertEqual(question, expected_question)
        self.assertIn(answer, expected)

    def test_ask_question_random(self):
        """Test ask_question with random question generation"""
        question, answer = ask_question("en")
        expected_questions = [
            "Will I pass this class",
            "Will tomorrow be a snow day",
            "Will I get the internship"
        ]
        expected_answer = [
            "Don't count on it",
            "Yes",
            "No",
            "Maybe",
            "Ask again later",
            "I doubt it",
            "Certainly",
            "I don't know"
        ]
        self.assertIn(question, expected_questions)
        self.assertIn(answer, expected_answer)

    def test_ask_question_invalid_language(self):
        """Test ask_question with an invalid language"""
        result = ask_question("fr") 
        self.assertEqual(result, [])

## testing shake_ball 
    def test_shake_ball_no_delay(self):
        """Test shake_ball with a valid language and no delay"""
        result = shake_ball("en", 0)
        expected = [
            "Don't count on it",
            "Yes",
            "No",
            "Maybe",
            "Ask again later",
            "I doubt it",
            "Certainly",
            "I don't know"
        ]
        self.assertIn(result, expected)

    def test_shake_ball_invalid_language(self):
        """Test shake_ball with an invalid language"""
        result = shake_ball("fr", 0)
        self.assertEqual(result, "invalid")

    def test_shake_ball_with_delay(self):
        """Test shake_ball with a valid language and 1 sec shake time"""
        result = shake_ball("en", 1)
        expected = [
            "Don't count on it",
            "Yes",
            "No",
            "Maybe",
            "Ask again later",
            "I doubt it",
            "Certainly",
            "I don't know"
        ]
        self.assertIn(result, expected)

    def test_shake_ball_non_integer_shake_time(self):
        """Test shake_ball with a non-integer shake time (i.e. a float)"""
        result = shake_ball("en", 1.5) 
        expected = [
            "Don't count on it",
            "Yes",
            "No",
            "Maybe",
            "Ask again later",
            "I doubt it",
            "Certainly",
            "I don't know"
        ]
        self.assertIn(result, expected)

if __name__ == "__main__":
    unittest.main()