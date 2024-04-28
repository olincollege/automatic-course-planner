import pandas as pd

df = pd.read_csv("predicted_schedule.csv", index_col=0).T

sem_courses = {
    "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
    "freshmen spring": ["QEA2", "ISIM", "P&M"],
    "sophomore fall": [
        "PIE",
        "ENGX2010: Quantitative Engineering Analysis 3",
        "ENGX2134: Engineering Systems Analysis (2cr)",
        "ENGR2360: Introduction to Thermal-Fluid Systems",
    ],
    "sophomore spring": [
        "CD",
        "Mechanics of Solids and Structures",
        "ENGR2340: Dynamics",
        "MTH3120: Partial Differential Equations",
    ],
    "junior fall": ["Mechanical Design", "Design for Manufacturing"],
    "junior spring": [],
    "senior fall": ["Capstone"],
    "senior spring": ["Capstone"],
}
courses_took = [
    "ENGX2000",
    "MTH1111/SCI1111",
    "ENGR1200",
    "AHSE0112",
    "ENGX2005",
    "ENGR1125",
    "AHSE1515",
    "ENGR2110",
    "ENGR2250",
    "ENGR3525",
    "ENGR3599A",
    "ENGR3220",
    "ENGR3599",
]

other_requirements = {
    "bio": ["SCI1270", "SCI1260/AHSE2160"],
    "design_depth": ["ENGR3210", "ENGR3290", "ENGR3250"],
    "probstat": ["MTH2130"],
    "matsci": ["SCI1440"],
}
other_requirements_fulfilled = {
    "bio": False,
    "design_depth": False,
    "probstat": False,
    "matsci": False,
}


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


# Example Usage
print(get_possible_semesters("ENGR1125"))


def fill_other_requirements(MAX_COURSES=4):
    for (
        course_type,
        courses,
    ) in other_requirements.items():  # courses is list of course number
        for course in courses:
            # among the semester the course would be offered,
            possible_semesters = get_possible_semesters(course)
            for semester in possible_semesters:
                # if the person is taking less courses than MAX_COURSES in the semester
                if (
                    len(sem_courses[semester]) < MAX_COURSES
                    and not other_requirements_fulfilled[course_type]
                ):
                    # fill in the sem_courses
                    course_title = df[course]["Course Title"]
                    sem_courses[semester].append(course_title)
                    # add it to the courses_took
                    courses_took.append(course)
                    other_requirements_fulfilled[course_type] = True
                    break
    return sem_courses


print(fill_other_requirements())
