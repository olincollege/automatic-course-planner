"""
Module: test_study_abroad.py

This module contains unit tests for the CourseModel class 
from the model.py module, specifically testing the functionality 
related to study abroad semesters.
"""

from model import CourseModel


def test_no_study_abroad():
    """
    Test case when no study abroad semester is specified.
    Expected output: No changes in the dataframe.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    coursemodel.fill_study_abroad()
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


def test_study_abroad_with_major():
    """
    Test case when study abroad semester is specified as junior spring with required major courses.
    Expected output: "Study Abroad: AHS" marked in the junior spring.
    """
    coursemodel = CourseModel("Mechanical Engineering", "N/A", "junior spring", "N/A")
    coursemodel.fill_major_required_courses()
    coursemodel.fill_study_abroad()
    expected_dic = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": [
            "QEA2",
            "ISIM",
            "P&M",
            "Mechanics of Solids and Structures",
        ],
        "sophomore fall": [
            "PIE",
            "ENGX2010: Quantitative Engineering Analysis 3",
            "ENGX2134: Engineering Systems Analysis (2cr)",
            "ENGR2360: Introduction to Thermal-Fluid Systems",
        ],
        "sophomore spring": [
            "CD",
            "ENGR2340: Dynamics",
            "MTH3120: Partial Differential Equations",
        ],
        "junior fall": ["Mechanical Design", "Design for Manufacturing"],
        "junior spring": [
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
        ],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_dic


def test_study_abroad_sophomore_fall_with_different_major():
    """
    Test case when study abroad semester is specified as
    Sophomore Fall with required major courses for different major.
    Expected output: "Study Abroad: AHS" marked in the Sophomore Fall semester,
    with correct major courses for MechE.
    """
    coursemodel = CourseModel(
        "Mechanical Engineering", "junior fall", "sophomore fall", "N/A"
    )
    coursemodel.fill_major_required_courses()
    coursemodel.fill_study_abroad()
    expected_dic = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": [
            "QEA2",
            "ISIM",
            "P&M",
            "Mechanics of Solids and Structures",
        ],
        "sophomore fall": [
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
        ],
        "sophomore spring": [
            "CD",
            "ENGR2340: Dynamics",
            "MTH3120: Partial Differential Equations",
        ],
        "junior fall": ["Mechanical Design", "Design for Manufacturing"],
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_dic
