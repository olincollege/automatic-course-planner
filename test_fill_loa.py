"""
Module: test_loa.py

This module contains unit tests for handling Leave of Absence (LOA) scenarios
in the CourseModel class from the model.py module.
"""

from model import CourseModel


def test_no_loa():
    """
    Test case for no Leave of Absence (LOA).
    Expected output: No changes in the dataframe.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    coursemodel.fill_loa()
    expected_dic = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": ["QEA2", "ISIM", "P&M"],
        "sophomore fall": ["PIE"],
        "sophomore spring": ["CD"],
        "junior fall": [],
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_dic


def test_loa_sophomore_fall():
    """
    Test case for LOA in sophomore fall.
    Expected output: LOA marked in sophomore fall semester.
    """
    coursemodel = CourseModel("N/A", "sophomore fall", "N/A", "N/A")
    coursemodel.fill_loa()
    expected_dic = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": ["QEA2", "ISIM", "P&M"],
        "sophomore fall": ["LOA", "LOA", "LOA", "LOA", "LOA"],
        "sophomore spring": ["CD"],
        "junior fall": [],
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_dic


def test_loa_senior_spring_major_courses():
    """
    Test case for LOA in senior spring with required major courses.
    Expected output: LOA marked in senior spring semester and major courses retained.
    """
    coursemodel = CourseModel("E: Computing", "senior spring", "N/A", "N/A")
    coursemodel.fill_loa()
    coursemodel.fill_major_required_courses()
    expected_dic = {
        "freshmen fall": [
            "QEA1",
            "Modsim",
            "DesNat",
            "AHS",
            "Human Factors Interface Design",
        ],
        "freshmen spring": [
            "QEA2",
            "ISIM",
            "P&M",
            "ENGR3525: Software Systems",
            "ENGR3599A: Special Topics in Computing: Data Structures Algorithms",
        ],
        "sophomore fall": ["PIE", "Special Topics in Computing: Computer Networks"],
        "sophomore spring": ["CD"],
        "junior fall": [],
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": ["LOA", "LOA", "LOA", "LOA", "LOA"],
    }
    assert coursemodel.sem_courses == expected_dic
