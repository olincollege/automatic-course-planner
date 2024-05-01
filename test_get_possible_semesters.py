"""
Module: test_get_possible_semesters.py

This module contains unit tests for the `get_possible_semesters` method 
of the CourseModel class from the model.py module. The method is responsible 
for determining the possible semesters in which a course can be taken.
"""

import pytest
from model import CourseModel


def test_get_possible_semesters_spring():
    """
    Test case for ENGR1125 in Spring semesters.
    Expected output: List of Spring semesters where the course can be taken.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_semesters("ENGR1125")
    assert result == [
        "freshmen spring",
        "sophomore spring",
        "junior spring",
        "senior spring",
    ]


def test_get_possible_semesters_fall():
    """
    Test case for ENGR1200 in Fall semesters.
    Expected output: List of Fall semesters where the course can be taken.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_semesters("ENGR1200")
    assert result == ["freshmen fall", "sophomore fall", "junior fall", "senior fall"]


def test_get_possible_semesters_all():
    """
    Test case for AHSE0112 in all semesters.
    Expected output: List of all semesters where the course can be taken.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_semesters("AHSE0112")
    assert result == [
        "freshmen fall",
        "freshmen spring",
        "sophomore fall",
        "sophomore spring",
        "junior fall",
        "junior spring",
        "senior fall",
        "senior spring",
    ]


def test_get_possible_semesters_multiple_areas():
    """
    Test case for SCI1260/AHSE2160 with multiple areas.
    Expected output: List of semesters where the course can be taken
        considering multiple areas.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_semesters("SCI1260/AHSE2160")
    assert result == [
        "freshmen spring",
        "sophomore fall",
        "sophomore spring",
        "junior fall",
        "junior spring",
        "senior fall",
        "senior spring",
        "freshmen fall",
    ]


def test_get_possible_semesters_empty_course_number():
    """
    Test case for an empty course number.
    Expected output: KeyError raised.
    """
    with pytest.raises(KeyError):
        coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
        coursemodel.get_possible_semesters("")


def test_get_possible_semesters_multiple_courses():
    """
    Test case for multiple courses.
    Expected output: ValueError raised.
    """
    with pytest.raises(ValueError):
        coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
        coursemodel.get_possible_semesters(["ENGR1200", "ENGR1125"])
