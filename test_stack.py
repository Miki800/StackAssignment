import pytest
from random import randrange
from stack import Stack

ORDERED_LIST = (1,2,3,4,5,6)
RANDOM_LIST = tuple([randrange(-10,10) for each in range(6)])

def _verify_largest(s):
    largest_element = max(s._data, key=lambda data_pair:data_pair[0])[0] 
    assert s.get_largest() == largest_element

@pytest.mark.parametrize(
    "lst", (ORDERED_LIST, RANDOM_LIST), ids=("ordered", "random"))
def test_largest(lst):
    s = Stack()
    for element in lst:
        s.push(element)
        _verify_largest(s)

@pytest.mark.parametrize(
    "lst", (ORDERED_LIST, RANDOM_LIST), ids=("ordered", "random"))
def test_push_pop(lst):
    s = Stack()
    for element in lst:
        s.push(element)
        assert s.peek() == element

    for element in lst[::-1]:
        assert s.pop() == element
