from model import CourseModel


def test_get_course_type_MTH():
    """
    Test case for MTH prefix.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_course_type("MTH2188A")
    assert result == "MTH"


def test_get_course_type_ENG():
    """
    Test case for ENG prefix.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_course_type("ENGR3390")
    assert result == "ENG"


def test_get_course_type_SCI():
    """
    Test case for SCI prefix.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_course_type("SCI1410")
    assert result == "SCI"


def test_get_course_type_AHS():
    """
    Test case for AHS prefix.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_course_type("AHSE1122")
    assert result == "AHS"


def test_get_course_type_empty():
    """
    Test case for empty input.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_course_type("")
    assert result is None


def test_get_course_type_other():
    """
    Test case for other prefixes.
    """
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_course_type("SUST3301")
    assert result is None
