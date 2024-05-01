from vivian_model import CourseModel


def test_E_C():
    """
    Test case for major E:C
    """
    coursemodel = CourseModel("E: Computing", "N/A", "N/A", "N/A")
    coursemodel.fill_major_required_courses()
    expected_output = {
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
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_output


def test_MechE():
    """
    Test case for major MechE
    """
    coursemodel = CourseModel("Mechanical Engineering", "N/A", "N/A", "N/A")
    coursemodel.fill_major_required_courses()
    expected_output = {
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
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_output


def test_ECE():
    """
    Test case for major ECE
    """
    coursemodel = CourseModel("Electrical Engineering", "N/A", "N/A", "N/A")
    coursemodel.fill_major_required_courses()
    expected_output = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": [
            "QEA2",
            "ISIM",
            "P&M",
            "ENGX2134: Engineering Systems Analysis (2cr)",
        ],
        "sophomore fall": [
            "PIE",
            "ENGX2010: Quantitative Engineering Analysis 3",
            "ENGR3410: Computer Architecture",
            "Robotics Systems Integration",
        ],
        "sophomore spring": [
            "CD",
            "Signals and Systems",
            "Intro Microelectronic Circuits with Lab",
            "ENGR3370:\xa0Controls",
        ],
        "junior fall": ["ENGR3420: Introduction to Analog and Digital Communication"],
        "junior spring": [],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_output
