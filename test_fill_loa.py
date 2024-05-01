import pandas as pd
import numpy as np
from model import CourseModel


def test_no_loa():
    # Test case: No LOA
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
    # Test case: LOA in Sophomore Fall
    coursemodel = CourseModel("N/A", "N/A", "sophomore fall", "N/A")
    coursemodel.fill_loa()
    expected_dic = pd.DataFrame(
        {
            "Freshmen Fall": ["", "", "", "", np.nan],
            "Freshmen Spring": ["", "", "", "", np.nan],
            "Sophomore Fall": ["LOA", "LOA", "LOA", "LOA", "LOA"],
            "Sophomore Spring": ["", "", "", "", np.nan],
            "Junior Fall": ["", "", "", "", np.nan],
            "Junior Spring": ["", "", "", "", np.nan],
            "Senior Fall": ["", "", "", "", np.nan],
            "Senior Spring": ["", "", "", "", np.nan],
        }
    )
    assert coursemodel.sem_courses == expected_dic


def test_loa_senior_spring_major_courses():
    # Test case: LOA in Senior Spring with required major courses
    coursemodel = CourseModel("E: Computing", "N/A", "Senior Spring", "N/A")
    coursemodel.fill_loa()
    coursemodel.fill_major_required_courses()
    expected_dic = pd.DataFrame(
        {
            "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS", np.nan],
            "Freshmen Spring": ["QEA2", "ISIM", "P&M", "Softdes", np.nan],
            "Sophomore Fall": ["PIE", "", "", "", np.nan],
            "Sophomore Spring": ["CD", "", "", "", np.nan],
            "Junior Fall": ["", "", "", "", np.nan],
            "Junior Spring": ["", "", "", "", np.nan],
            "Senior Fall": ["Capstone", "", "", "", np.nan],
            "Senior Spring": ["LOA", "LOA", "LOA", "LOA", "LOA"],
        }
    )
    assert coursemodel.sem_courses == expected_dic
