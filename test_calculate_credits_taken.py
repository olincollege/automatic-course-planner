import pytest

# Import the function to be tested
from model import calculate_credits_taken


# Define the test cases
@pytest.mark.parametrize(
    "courses_dict, expected_credits_took",
    [
        # Test case covering basic functionality with known inputs and outputs
        (
            {
                "Freshmen Fall": ["ENGR4190", "ENGR3392", "MTH2199", "AHSE1122"],
                "Freshmen Spring": ["SCI2210", "SCI1240", "MTH2188", "ENGX2000"],
                "Sophomore Fall": ["ENGX2005", "ENGX2199", "ENGR3810", "ENGR3599B"],
                "Sophomore Spring": ["ENGR3440", "ENGR3250", "ENGR2320", "ENGR1200"],
                "Junior Fall": ["ENGR3299", "SCI1230", "SCI2220", "SCI3320"],
                "Junior Spring": ["SUST3301", "MTH3199", "", ""],
                "Senior Fall": ["ENGX2199", "", "", ""],
                "Senior Spring": ["ENGR3640", "", "", ""],
            },
            {"AHSE": 4, "ENGR": 56, "MTH/SCI": 28, "MTH": 12, "OFYI": 0, "TOTAL": 88},
        ),
        # Add more test cases here to cover various scenarios and edge cases
        # Test case with empty courses dictionary
        ({}, {"AHSE": 0, "ENGR": 0, "MTH/SCI": 0, "MTH": 0, "OFYI": 0, "TOTAL": 0}),
        # Test case with one semester and one course
        (
            {"Freshmen Fall": ["ENGR4190"]},
            {"AHSE": 0, "ENGR": 4, "MTH/SCI": 0, "MTH": 0, "OFYI": 0, "TOTAL": 4},
        ),
        # Test case with a course contributing to multiple areas
        (
            {"Junior Spring": ["ENGR2199B/MTH2188B"]},
            {"AHSE": 0, "ENGR": 2, "MTH/SCI": 2, "MTH": 2, "OFYI": 0, "TOTAL": 4},
        ),
        # Add more test cases as needed to cover other scenarios
    ],
)
def test_calculate_credits_taken(courses_dict, expected_credits_took):
    """
    Test the calculate_credits_taken function.

    Args:
        courses_dict: Input dictionary with semesters as keys and lists of course numbers
            as values for each key.
        expected_credits_took: Expected output dictionary indicating credits taken for each area.
    """
    # Call the function to get the actual result
    actual_credits_took = calculate_credits_taken(courses_dict)

    # Check if the actual result matches the expected result
    assert actual_credits_took == expected_credits_took
