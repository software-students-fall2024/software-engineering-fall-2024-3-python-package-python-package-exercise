from oracle.fortune_cookie import get_fortune, fortunes
    
#test function
def test_fortune_cookie():
    result = get_fortune()
    assert result in fortunes

def test_fortune_is_string():
    result = get_fortune()
    assert isinstance(result, str)

def test_fortunes_not_empty():
    assert len(fortunes)>0
