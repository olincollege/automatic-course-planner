from vivian_model import CourseModel


def test_calculate_credits_taken_default():
    """
    Test case for default required courses
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    coursemodel.calculate_credits_taken()
    expected_output = {
        "AHS": 16,
        "ENG": 44,
        "MTH/SCI": 36,
        "MTH": 8,
        "SCI": 0,
        "OFYI": 1,
        "TOTAL": 69,
    }
    assert coursemodel.credits_took == expected_output


def test_calculate_credits_taken_with_major():
    """
    Test case for required major courses with a specified major
    """
    coursemodel = CourseModel("Mechanical Engineering", "N/A", "N/A", "N/A")
    coursemodel.fill_major_required_courses()
    coursemodel.calculate_credits_taken()
    expected_output = {
        "AHS": 16,
        "ENG": 72,
        "MTH/SCI": 68,
        "MTH": 12,
        "SCI": 0,
        "OFYI": 1,
        "TOTAL": 101,
    }
    assert coursemodel.credits_took == expected_output


def test_calculate_credits_taken_other_requirements():
    """
    Test case for all required courses filled up
    """
    coursemodel = CourseModel("E: Computing", "N/A", "N/A", "N/A")
    coursemodel.fill_major_required_courses()
    coursemodel.fill_other_requirements()
    coursemodel.calculate_credits_taken()
    expected_output = {
        "AHS": 16,
        "ENG": 68,
        "MTH/SCI": 68,
        "MTH": 12,
        "SCI": 4,
        "OFYI": 1,
        "TOTAL": 101,
    }

    assert coursemodel.credits_took == expected_output


def test_calculate_credits_taken_final():
    """
    Test case for all course schedule filled up, checking for total credits took
    greater than required minimum credits (120).
    """
    coursemodel = CourseModel("Mechanical Engineering", "N/A", "N/A", "N/A")
    coursemodel.fill_major_required_courses()
    coursemodel.fill_other_requirements()
    coursemodel.fill_empty_schedules()
    coursemodel.calculate_credits_taken()
    assert (coursemodel.credits_took["TOTAL"]) >= 120


def test_calculate_credits_taken_final_with_options():
    """
    Test case for all course schedule filled up with study abroad and early graduation,
    checking for total credits took greater than required minimum credits (120).
    """
    coursemodel = CourseModel(
        "Electrical Engineering", "N/A", "junior spring", "One semester early"
    )
    coursemodel.fill_loa()
    coursemodel.fill_major_required_courses()
    coursemodel.fill_grad_early()
    coursemodel.fill_study_abroad()
    coursemodel.fill_other_requirements()
    coursemodel.fill_empty_schedules()
    coursemodel.calculate_credits_taken()
    assert (coursemodel.credits_took["TOTAL"]) >= 120
