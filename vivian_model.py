"""
CREATES STUDENT SCHEDULE WITH THE PREDICTION MODEL
"""

import pandas as pd


class CourseModel:
    def __init__(self):
        pass

    def get_required_courses(major, study_abroad):
        df = pd.DataFrame(
            None,
            index=range(5),
            columns=[
                "Semester 1",
                "Semester 2",
                "Semester 3",
                "Semester 4",
                "Semester 5",
                "Semester 6",
                "Semester 7",
                "Semester 8",
            ],
        )
        sem_courses = {}

        if major == "E: Computing":
            sem_courses = {
                "Semester 1": ["QEA1", "Modsim", "DesNat", "AHS Concentration"],
                "Semester 2": ["QEA2", "ISIM", "Products & Markets", "Softdes"],
                "Semester 3": ["PIE"],
                "Semester 4": ["CD", "SoftSys"],
                "Semester 5": [],
                "Semester 6": [],
                "Semester 7": ["Senior Capstone"],
                "Semester 8": ["Senior Capstone"],
            }
        elif major == "Mechanical Engineering":
            pass
        elif major == "Electrical Engineering":
            pass
        elif major == "E: Robo":
            pass
        else:
            print("Choose a different major")
        for semester, courses in sem_courses.items():
            for i, course in enumerate(courses):
                df.at[i, semester] = course

        if study_abroad == "Yes":
            df.at[1, "Semester 6"] = "Study Abroad"

        df = df.fillna("")
        return df
