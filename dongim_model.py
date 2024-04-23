# my_model.py

import pandas as pd
import random


def create_student_schedule(major, study_abroad_semesters, electives):

    sem_courses = {}

    # Define default course names
    if major == "E: Computing":
        sem_courses = {
            "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS"],
            "Freshmen Spring": ["QEA2", "ISIM", "P&M", "SoftDes"],
            "Sophomore Fall": ["PIE", "Discrete", "", ""],
            "Sophomore Spring": ["CD", "SoftSys", "", ""],
            "Junior Fall": ["Bio", "MatSci", "", ""],
            "Junior Spring": ["", "", "", ""],
            "Senior Fall": ["Capstone", "", "", ""],
            "Senior Spring": ["Capstone", "", "", ""],
        }
        sem_courses["Sophomore Fall"][2] = random.choices(
            ["FoCS", "CompRobo"], weights=(90, 10, 50)
        )[0]

    elif major == "E: Robo":
        pass

    elif major == "MechE":
        pass

    # Create an empty DataFrame with 4 rows and 8 columns
    data = pd.DataFrame(index=range(1, 5), columns=sem_courses.keys())

    # Fill in course names for each semester
    for col, courses in zip(sem_courses.keys(), sem_courses.values()):
        data[col] = courses

    # Change index name to "Study Abroad" for specified semesters
    for semester in study_abroad_semesters:
        data = data.rename(columns={semester: f"{semester} (Study Abroad)"})

    for course in electives:
        data.loc[course[0][0], course[0][1]] = course[1]

    return data
