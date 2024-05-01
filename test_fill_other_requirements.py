from vivian_model import CourseModel


def test_fill_other_requirements_basic_schedule_major_specified():
    """
    Test case with a basic schedule and major specified.
    Expected output: Other requirements filled in according to the specified major.
    """
    coursemodel = CourseModel("Electrical Engineering", "N/A", "N/A", "N/A")
    coursemodel.fill_major_required_courses()
    coursemodel.fill_grad_early()
    coursemodel.fill_study_abroad()
    coursemodel.fill_other_requirements()
    expected_sem_courses = {
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
        "junior fall": [
            "ENGR3420: Introduction to Analog and Digital Communication",
            "SCI1260_AHSE2160: The Intersection of Biology, Art and Technology",
            "Human Factors Interface Design",
        ],
        "junior spring": [
            "MTH2136 / SCI2136: Astronomy and Statistics: AstroStats",
            "SCI1320: Paper Panacea: Part I with Laboratory",
        ],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_sem_courses


def test_fill_other_requirements_with_study_abroad():
    """
    Test case with study abroad.
    Expected output: Other requirements filled in with study abroad included.
    """
    coursemodel = CourseModel("E: Computing", "N/A", "junior fall", "N/A")
    coursemodel.fill_major_required_courses()
    coursemodel.fill_grad_early()
    coursemodel.fill_study_abroad()
    coursemodel.fill_other_requirements()
    expected_sem_courses = {
        "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
        "freshmen spring": ["QEA2", "ISIM", "P&M", "ENGR3525: Software Systems"],
        "sophomore fall": [
            "PIE",
            "Human Factors Interface Design",
            "Special Topics in Computing: Computer Networks",
            "Human Factors Interface Design",
        ],
        "sophomore spring": [
            "CD",
            "ENGR3599A: Special Topics in Computing: Data Structures Algorithms",
            "ENGR3235_or_SCI2235: Biomimicry",
            "MTH2136 / SCI2136: Astronomy and Statistics: AstroStats",
        ],
        "junior fall": [
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
            "Study Abroad: AHS",
        ],
        "junior spring": ["SCI1320: Paper Panacea: Part I with Laboratory"],
        "senior fall": ["Capstone"],
        "senior spring": ["Capstone"],
    }
    assert coursemodel.sem_courses == expected_sem_courses


def test_fill_other_requirements_with_early_graduation():
    """
    Test case with early graduation.
    Expected output: Other requirements filled in with early graduation included.
    """
    coursemodel = CourseModel(
        "Mechanical Engineering", "N/A", "N/A", "One semester early"
    )
    coursemodel.fill_major_required_courses()
    coursemodel.fill_grad_early()
    coursemodel.fill_study_abroad()
    coursemodel.fill_other_requirements()
    expected_sem_courses = {
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
            "Mechanics of Solids and Structures",
            "ENGR3235_or_SCI2235: Biomimicry",
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
            "MTH2136 / SCI2136: Astronomy and Statistics: AstroStats",
            "SCI1320: Paper Panacea: Part I with Laboratory",
        ],
        "junior fall": ["Mechanical Design", "Design for Manufacturing"],
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
    assert coursemodel.sem_courses == expected_sem_courses
