import pytest
from models import Course



def test_credits():
    test_course = Course("WebDev", "Tim", 4)
    assert test_course.creditLimit(test_course.credits) is True 

def test_invalid_credits():
    test_course = Course("Webdev", "Tim", 8)
    assert test_course.creditLimit(test_course.credits) is False

def test_invalid_credit():
    with pytest.raises(AttributeError):
        Course("WebDev", "Tim", "3")
def test_invalid_name():
    with pytest.raises(AttributeError):
        Course("webdev", 7, 3)
