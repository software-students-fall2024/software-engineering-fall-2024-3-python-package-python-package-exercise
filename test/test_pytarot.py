import pytest

# import src.pytarot.truelover as truelover_module
# import src.pytarot.luckyday as luckyday_module
# import src.pytarot.answersofwisdom as answers_of_wisdom_module
from src.pytarot import get_answers_of_wisdom, get_lucky_day, get_true_lover




class Tests:
    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #

    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    #true lover tests

    def test_get_true_lover_non_empty(self):
        """
        Verify get_true_lover() function and make sure it returns a non-empty string.
        """
        result =  get_true_lover()
        
        # Check that the result is a non-empty string
        assert isinstance(result, str), "The result should be a string."
        assert len(result) > 0, "The result should not be an empty string."

    def test_get_true_lover_content(self):
        """
        Verify get_true_lover() function and make sure it contains all the necessary elements.
        """
        result = get_true_lover()
        
        # Check for content
        jobs = ["Teacher", "Engineer", "Doctor", "Nurse", "Architect", "Software Developer", "Graphic Designer", "Chef", "Pilot", 
                "Lawyer", "Accountant", "Scientist", "Electrician", "Carpenter", "Mechanic", "Writer", "Artist", "Photographer", 
                "Pharmacist", "Veterinarian", "Social Worker", "Police Officer", "Firefighter", "Librarian", "Journalist", 
                "Marketing Specialist", "Salesperson", "Plumber", "Psychologist", "Data Analyst", "Financial Advisor", "Dentist", 
                "Actor", "Musician", "Farmer", "Translator", "Consultant", "Project Manager", "Researcher", "Event Planner", 
                "Web Developer", "Therapist", "Fitness Trainer", "Fashion Designer", "Interior Designer", "Animator", "Biologist", 
                "Chemist", "Historian"]
        
        heights = ["Very Short", "Short", "Below Average", "Average", "Above Average", "Tall", "Very Tall", "Extremely Tall"]
        eye_colors = ["Brown", "Blue", "Green", "Hazel", "Amber", "Gray", "Violet", "Black", "Red"]
        hair_colors = ["Black", "Brown", "Blonde", "Red", "Auburn", "Chestnut", "Gray", "White", "Silver", "Platinum Blonde", 
                    "Strawberry Blonde", "Blue", "Green", "Pink", "Purple", "Teal"]
        residences = ["House", "Apartment", "Condo", "Villa", "Cabin", "Cottage", "Mansion", "Farmhouse", "Bungalow", "Duplex", 
                    "Studio", "Loft", "Townhouse", "Mobile Home", "Penthouse", "Dormitory", "Hostel", "Boarding House", 
                    "Tiny House", "Yurt", "Chalet", "Tent", "RV", "Boat", "Caravan", "Castle", "Ranch", "Hut", "Treehouse", 
                    "Igloo", "Palace"]

        # Ensure that the output has all the elements
        assert any(job in result for job in jobs), "The result should contain a job title."
        assert any(height in result for height in heights), "The result should contain a height descriptor."
        assert any(eye_color in result for eye_color in eye_colors), "The result should contain an eye color."
        assert any(hair_color in result for hair_color in hair_colors), "The result should contain a hair color."
        assert any(residence in result for residence in residences), "The result should contain a residence type."

    def test_get_true_lover_uniqueness(self):
        """
        Verify get_true_lover() function and make sure it has some uniqueness to its output.
        """
        results = {get_true_lover() for _ in range(10)}
        assert len(results) > 1, "The function should generate some unique profiles."

    def test_get_true_lover_format_keywords(self):
        """
        Verify get_true_lover() function and make sure it has the mandatory keywords in the output.
        """
        result = get_true_lover()
        expected_keywords = ["who is", "with", "eyes", "hair", "lives in"]
        for keyword in expected_keywords:
            assert keyword in result, f"The result should contain '{keyword}'"


