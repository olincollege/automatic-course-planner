import pandas as pd


def get_course_type(course):
    """
    Determine the course type based on its prefix
    Args:
        course(str): Course code (e.g., 'MTH101', 'ENGR200')
    Returns:
        str: Course type ('MTH', 'ENG', 'SCI', 'AHS') or None if not matched
    """
    if course.startswith("MTH"):
        return "MTH"
    elif course.startswith("ENG"):
        return "ENG"
    elif course.startswith("SCI"):
        return "SCI"
    elif course.startswith("AHS"):
        return "AHS"
    else:
        return None


def get_possible_courses(semester, df):
    """
    Get possible course for each semester as a dictionary along with its likelihood of offering
    Args:
        semester(str): semester that you want to check the course offering for (e.g., 'freshman fall')
        df (DataFrame): DataFrame containing the course offering data
    Returns:
        course offering dictionary with likelihood, separated by course type
    """
    # Initialize an empty dictionary to store offered courses by type
    offered_courses = {"MTH": {}, "ENG": {}, "SCI": {}, "AHS": {}}

    # Find the corresponding column index for the semester
    semester_column = semester.lower()

    # Check if the semester column exists in the DataFrame
    if semester_column in df.columns:
        # Filter the DataFrame for courses offered in the specified semester with values greater than 0.5
        courses_offered = df[df[semester_column] > 0.5]

        # Iterate through the courses offered and categorize them by type
        for course in courses_offered.index.tolist():
            course_type = get_course_type(course)
            if course_type:
                offered_courses[course_type][course] = courses_offered.loc[
                    course, semester_column
                ]

    return offered_courses


def get_possible_semesters(course_number):
    """
    Extracts semesters with a likelihood greater than 0.5 for a given course number ordered by likelihood.

    Args:
        df (DataFrame): DataFrame containing the likelihood of the course being offered for different semesters.
        course_number (str): The course number for which semesters are to be extracted.

    Returns:
        list: An ordered list of semesters with likelihood greater than 0.5 for the given course number.
    """
    # Remove the first element (Course Title) from the row and make it into DataFrame
    possible_semesters_df = pd.DataFrame(df[course_number][1:])

    # Reset the index to have the semester as a column
    possible_semesters_df.reset_index(inplace=True)
    possible_semesters_df.columns = ["Semester", "Likelihood"]

    # Sort the DataFrame by Likelihood in ascending order
    possible_semesters_df = possible_semesters_df.sort_values(
        by="Likelihood", ascending=False
    )

    # Filter the DataFrame to select semesters with likelihood > 0.5
    possible_semesters = possible_semesters_df[
        possible_semesters_df["Likelihood"] > 0.5
    ]["Semester"].tolist()

    return possible_semesters
