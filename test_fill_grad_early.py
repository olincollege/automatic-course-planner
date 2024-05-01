import pandas as pd
from vivian_model import CourseModel


def test_grad_early_na():
    """
    Test case when graduation is not specified.
    Expected output: No changes in the dataframe.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    coursemodel.fill_grad_early()
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


def test_grad_early_one_semester():
    """
    Test case when graduation is specified as one semester early.
    Expected output: "Already Graduated!" marked in Senior Spring semester.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "One semester early")
    coursemodel.fill_grad_early()
    expected_dic = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": ["QEA2", "ISIM", "P&M"],
        "sophomore fall": ["PIE"],
        "sophomore spring": ["CD"],
        "junior fall": [],
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": [
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
        ],
    }
    assert coursemodel.sem_courses == expected_dic


def test_grad_early_one_year_with_major():
    """
    Test case when graduation is specified as one year early with required major courses.
    Expected output: "Already Graduated!" marked in Senior Fall and Spring semesters.
    """
    coursemodel = CourseModel("E: Computing", "N/A", "N/A", "One year early")
    coursemodel.fill_major_required_courses()
    coursemodel.fill_grad_early()
    expected_dic = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": ["QEA2", "ISIM", "P&M", "ENGR3525: Software Systems"],
        "sophomore fall": [
            "PIE",
            "Human Factors Interface Design",
            "Special Topics in Computing: Computer Networks",
        ],
        "sophomore spring": [
            "CD",
            "ENGR3599A: Special Topics in Computing: Data Structures Algorithms",
        ],
        "junior fall": [],
        "junior spring": [],
        "senior fall": [
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
        ],
        "senior spring": [
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
        ],
    }
    assert coursemodel.sem_courses == expected_dic


def test_grad_early_one_semester_with_major_and_study_abroad():
    """
    Test case when graduation is specified as one semester early with required major courses and study abroad.
    Expected output: "Already Graduated!" marked in Senior Spring semester, study abroad marked in Junior Fall semester.
    """
    coursemodel = CourseModel(
        "E: Computing", "N/A", "junior fall", "One semester early"
    )
    coursemodel.fill_major_required_courses()
    coursemodel.fill_study_abroad()
    coursemodel.fill_grad_early()
    expected_dic = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": ["QEA2", "ISIM", "P&M", "ENGR3525: Software Systems"],
        "sophomore fall": [
            "PIE",
            "Human Factors Interface Design",
            "Special Topics in Computing: Computer Networks",
        ],
        "sophomore spring": [
            "CD",
            "ENGR3599A: Special Topics in Computing: Data Structures Algorithms",
        ],
        "junior fall": [
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
        ],
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": [
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
            "Graduating Early!",
        ],
    }
    assert coursemodel.sem_courses == expected_dic
