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
    # Test case: LOA in Senior Spring with required major courses
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
