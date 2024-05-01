import pytest
from vivian_model import CourseModel


def test_get_possible_semesters_ENGR1125():
    # Test case for ENGR1125 in Spring semesters
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_semesters("ENGR1125")
    assert result == [
        "freshmen spring",
        "sophomore spring",
        "junior spring",
        "senior spring",
    ]


def test_get_possible_semesters_ENGR1200():
    # Test case for ENGR1200 in Fall semesters
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_semesters("ENGR1200")
    assert result == ["freshmen fall", "sophomore fall", "junior fall", "senior fall"]


def test_get_possible_semesters_AHSE0112():
    # Test case for AHSE0112 in all semesters
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


def test_get_possible_semesters_SCI1260_AHSE2160():
    # Test case for SCI1260/AHSE2160 with multiple areas
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
    # Test case for an empty course number
    with pytest.raises(KeyError):
        coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
        coursemodel.get_possible_semesters("")


def test_get_possible_semesters_multiple_courses():
    # Test case for multiple courses
    with pytest.raises(ValueError):
        coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
        coursemodel.get_possible_semesters(["ENGR1200", "ENGR1125"])
