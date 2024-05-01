import pytest
from vivian_model import CourseModel


def test_get_possible_courses_freshmen_fall():
    """
    Test case for freshmen fall semester.
    """
    # Expected output for freshmen fall semester with the input as lowercases
    expected_output = {
        "MTH": {
            "MTH1111/SCI1111": 0.99981566170061,
            "MTH2110": 0.9948004286591527,
            "MTH2135/ENGR3635": 0.5609783815439279,
            "MTH3120": 1.0000001985057518,
        },
        "ENG": {
            "ENGR1200": 0.99981566170061,
            "ENGR1330": 0.8722760999626119,
            "ENGR2110": 0.8620054163390886,
            "ENGR2141/AHSE2141": 0.571290194365154,
            "ENGR2250": 1.0000001985057518,
            "ENGR2299": 0.6129744236451242,
            "ENGR2360": 0.55,
            "ENGR3199": 0.52876719391148,
            "ENGR3220": 0.8126774445830195,
            "ENGR3260": 0.9272335473040588,
            "ENGR3260L": 0.9432309075217344,
            "ENGR3290": 1.0,
            "ENGR3299A": 0.8002192474813353,
            "ENGR3330": 0.5454896345790194,
            "ENGR3350": 0.5729082071644458,
            "ENGR3355": 0.9999999999992432,
            "ENGR3365": 0.9999999999992432,
            "ENGR3392": 1.1068637359756508,
            "ENGR3410": 0.99981566170061,
            "ENGR3420": 0.7708220257967873,
            "ENGR3426": 0.5923392072550049,
            "ENGR3499": 0.6995606500057383,
            "ENGR3520": 1.026904331771547,
            "ENGR3599": 1.0000823896909228,
            "ENGR4190": 1.0,
            "ENGR4290": 1.0,
            "ENGR4599": 0.9126277712381836,
            "ENGX2000": 0.8788545015438982,
            "ENGX2010": 0.9344201224052324,
            "ENGX2134": 0.9999999999992432,
        },
        "SCI": {
            "SCI1260/AHSE2160": 0.9999999999992432,
            "SCI1270": 0.8818610664732737,
            "SCI1410": 0.6608807389168082,
            "SCI1440": 0.9017772577954374,
        },
        "AHS": {
            "AHSE0112": 1.0,
            "AHSE1122": 0.894167845140597,
            "AHSE1155": 0.6834414333350782,
            "AHSE1160": 0.9197698262255724,
            "AHSE1199": 0.8474038327397033,
            "AHSE1515": 1.0000000969903182,
            "AHSE2135": 0.8818610664732737,
            "AHSE2150_SCI1250": 0.9999999999992432,
            "AHSE2199": 0.6865369575942863,
            "AHSE2199A": 0.5106408293586517,
            "AHSE2199B": 0.8308775981863217,
            "AHSE2515": 0.9523862030671012,
            "AHSE3190": 1.0,
            "AHSE4190": 1.00000011179658,
        },
    }
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_courses("freshmen fall")
    assert result == expected_output


def test_get_possible_courses_junior_spring():
    """
    Test case for junior spring semester.
    """
    # Expected output for junior spring semester with the input as a mix of upper and lowercases
    expected_output = {
        "MTH": {"MTH2136/SCI2136": 0.5055351037611402, "MTH3120": 1.0000001985092457},
        "ENG": {
            "ENGR1125": 0.8380087818922336,
            "ENGR1330": 0.9019584240636206,
            "ENGR2250": 1.0000001985092457,
            "ENGR2320": 0.648148101467063,
            "ENGR2330": 0.8928863740914261,
            "ENGR2340": 0.8138965542073863,
            "ENGR2410": 0.8362569222029531,
            "ENGR2420": 0.8813025996135881,
            "ENGR2510": 0.7985392004512515,
            "ENGR3210": 0.5775564441507329,
            "ENGR3240": 0.6116051077325536,
            "ENGR3290": 1.0,
            "ENGR3350": 0.7981660515512119,
            "ENGR3355": 1.0000000000003757,
            "ENGR3365": 1.0000000000003757,
            "ENGR3370": 0.6928823469181264,
            "ENGR3390": 0.8380106848441827,
            "ENGR3392": 1.015547258371487,
            "ENGR3520": 0.9816095051013828,
            "ENGR3525": 0.8065727403136833,
            "ENGR3531/MTH2131": 0.7123592202710116,
            "ENGR3599": 1.0000532097253594,
            "ENGR3599A": 0.5126221551401446,
            "ENGR4190": 1.0,
            "ENGR4290": 1.0,
            "ENGR4599": 0.9126261341298476,
            "ENGX2005": 0.7748256270938197,
            "ENGX2134": 1.0000000000003757,
        },
        "SCI": {
            "SCI1260/AHSE2160": 1.0000000000003757,
            "SCI1320": 0.6306309686376972,
            "SCI1440": 1.0216002648405258,
        },
        "AHS": {
            "AHSE0112": 1.0,
            "AHSE1515": 1.0000000646619362,
            "AHSE2150_SCI1250": 1.0000000000003757,
            "AHSE2199": 0.6457605705487106,
            "AHSE2199A": 0.9302973908851812,
            "AHSE2199B": 0.7723150037623578,
            "AHSE2515": 0.9047792535426394,
            "AHSE3190": 1.0,
            "AHSE4190": 1.000000074532544,
        },
    }
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_courses("Junior Spring")
    assert result == expected_output


def test_get_possible_courses_empty_string():
    """
    Test case for empty string input.
    """
    # Expected output for empty string input
    expected_output = {"MTH": {}, "ENG": {}, "SCI": {}, "AHS": {}}
    coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
    result = coursemodel.get_possible_courses("")
    assert result == expected_output


def test_get_possible_courses_multiple_semesters():
    """
    Test case for multiple semesters input.
    """
    # Check if AttributeError is raised for multiple semesters input
    with pytest.raises(AttributeError):
        coursemodel = CourseModel("N/A", "N/A", "N/A", "N/A")
        coursemodel.get_possible_courses(["freshmen fall", "junior spring"])
