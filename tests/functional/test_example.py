import pytest
from models import Course, Registration
from flask import json



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

def test_id():
    test_id = Registration(2, 4)
    assert test_id.student_id == 2

def test_invalid_type():
    with pytest.raises(AttributeError):
        Registration("2", 4)

