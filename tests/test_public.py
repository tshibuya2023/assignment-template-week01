import pytest
from src.solution import fibonacci

def test_small():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5

@pytest.mark.timeout(1)
def test_medium():
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
