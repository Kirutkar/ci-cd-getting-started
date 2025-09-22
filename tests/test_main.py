from src.main import add

def test_add_func():
    assert add(3,3) == 6
    assert add(4,5) == 9
    assert add(0,0) == 0