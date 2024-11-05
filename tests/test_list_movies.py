from pyquotes.list_movies import list_movies
def test_list_movies_returns_list():
    movies = list_movies()
    assert isinstance(movies, list), "return a list"

def test_list_movies_contains_strings():
    movies = list_movies()
    assert all(isinstance(movie, str) for movie in movies), "each title should be string"

def test_list_movies_no_duplicates():
    movies = list_movies()
    assert len(movies) == len(set(movies)), "list should not contain duplicates"
