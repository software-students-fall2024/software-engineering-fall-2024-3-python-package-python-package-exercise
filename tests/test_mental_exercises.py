import unittest
from codebreak.mental_exercises import mental_exercise  

class TestMentalExercise(unittest.TestCase):

    def test_focus_exercise(self):
        """Test that a valid exercise is returned for 'focus' break_type."""
        result = mental_exercise("focus")
        self.assertIsInstance(result, str)
        self.assertIn(result, [
            "Close your eyes and take five deep breaths, focusing on the inhale and exhale.",
            "Practice the 4-7-8 breathing technique: inhale for 4 seconds, hold for 7, exhale for 8.",
            "Try a quick counting meditation: count down from 100 by 3s to refocus your mind.",
            "Visualize a peaceful place and imagine yourself there for one minute, focusing on each detail.",
            "Trace the shape of an object on your desk with your eyes, noticing its edges and curves.",
            "Recite a positive affirmation slowly, like 'I am focused and relaxed,' three times.",
            "Look at a nearby plant or picture and observe it closely for 60 seconds.",
            "Mentally list three things you're grateful for today and focus on each one for a moment.",
            "Imagine yourself completing your next task successfully and feel the sense of accomplishment.",
            "Spend a minute focusing on the sensations in your body, starting from head to toe.",
            "Do a 30-second eye massage with gentle pressure, focusing on relaxing your eyes."
        ])

    def test_creativity_exercise(self):
        """Test that a valid exercise is returned for 'creativity' break_type."""
        result = mental_exercise("creativity")
        self.assertIsInstance(result, str)
        self.assertIn(result, [
            "Write down three new ideas you would like to explore in your next project.",
            "Draw a quick doodle of something you find inspiring.",
            "Think of a new feature you'd add to your favorite app and jot down a few details.",
            "Create a quick list of five alternative uses for a common object near you.",
            "Sketch a quick design for a completely fictional product.",
            "Write down a random word, and think of five ways it relates to your current project.",
            "Challenge yourself to come up with a different way to solve a common daily problem.",
            "Write a short two-sentence story with a plot twist at the end.",
            "Invent a new flavor combination for a dessert or snack.",
            "List as many creative uses for a paperclip as you can think of in one minute.",
            "Imagine an alternate universe where your project is used in an unexpected way."
        ])

    def test_mindfulness_exercise(self):
        """Test that a valid exercise is returned for 'mindfulness' break_type