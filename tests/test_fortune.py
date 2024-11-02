import pytest
from src.fortune.FortuneCookie import quoteGetter, customFortuneCookie, addQuote, fortuneCookie, randomFortuneCookie
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Tests:

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

    def test_customFortuneCookie(self, capsys):
        """
        Verify customFortuneCookie() function and make sure it returns a non-empty string.
        Note that for example purposes, we have not used the example_fixture in this test functino.
        """

        for i in range(100):
            test_outputImage = f"""                                                                                                    
                                                                                                        
                                                                                                        
                                                                                                        
                                .@@*#@+%#...........                                                 
                            ..@*+=========####*++@@@..                                                
                            .@@==--===+==--===#=======+++.                                              
                        .@+==------==*@=---=@#===----==+@.                                            
                        .@===-:::::--==+%%=---==+==------==+@.                           =@@-=#@        
                    @-==--::---:-===+#*=---=====---:---==++.              .:@=@%=...........%.       
                    +@===---------=====@*=-----==----::--====%....... @@:.=++:................@.       
                    @===---------======*@*=----------:::@--====@@%#=%.........................:@        
                .@===--------==@=====@%@=---------::::---====@%@..........................:+=*        
                =#===-------=========+#*@=-------:::::---=====+*+....An exciting opportunity lies ahead of you......#.        
                :@==--------==========%%@=----------::----====+@#=...........................=@.        
                @==-------====*======@%@==--------:::----=====+@#...........................-*-.        
                @==-------==+%#===-==+##@=-------::::---======+*%=..........==###%@%##-..==#@@@..        
                @==-------==+#*#=====#@@@=@-----:::::---==-====@@@..........==@@@*=*@@=...........        
                @==-----====+#+=====#@@=*=----::-::---======++@#+%@%@+........                            
                %+==----===#+#=====##@..%=------::----======+=@%..                                         
                #+=========#@*==+@@@....=----:::::---=======+@@...                                         
                .@*++========%+++@%......@=--::::::-@====@=++@@..                                            
                %+++######+++@@...     .+=--::::--=======+%@@...                                            
                @+#@@##++@@.           .@-::----======+++-#@..                                              
                .*+#@#@   ..           @=#@--=======@+#=@+%...                                              
                                    @=@=======+++@@@#@:.                                                 
                                    @+===+%=+++#%@@+@..                                                  
                                    ++=====##@#@#@@@..                                                   
                                    .#+++##@@%%@@@....                                                   
                                    .##%@@@@@@#@...                                                      
                                    .:+@*@@@+@.                                                          
                                    .. %@@@...                                                           
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        """
            customFortuneCookie("An exciting opportunity lies ahead of you.")
            actual_captured = capsys.readouterr()
            assert (".@@*#@+%#" in actual_captured.out), f"Expected the text printed by customFortuneCookie() contain an ASCII image."
            assert ("An exciting opportunity lies ahead of you." in actual_captured.out), f"Expected the text printed by customFortuneCookie() to contain the input quote: 'An exciting opportunity lies ahead of you.'"

    def test_addQuote(self):

        quotes = [
            "The best way to predict the future is to create it.",
            "Happiness is not something ready-made. It comes from your own actions.",
            "You will find great success in your endeavors.",
            "Your hard work will soon pay off.",
            "Adventure awaits you around the corner.",
            "Believe you can and you're halfway there.",
            "A friend is someone who knows all about you and still loves you.",
            "The only limit to our realization of tomorrow is our doubts of today.",
            "You will make a change for the better.",
            "Your talents will be recognized and suitably rewarded."
        ]

        """
        Verify addQuote() function and make sure it returns a non-empty string.
        Note that for example purposes, we have not used the example_fixture in this test functino.
        """
        
        for i in range(10):
            addQuote(quotes[i], "g")
            f = open("GoodFortune.txt", "r")
            content = f.read()
            assert (quotes[i] in content), f"Expected the new quote in GoodFortune text file."
    def test_1(self):
        assert True  # Replace with actual tests