"""
CREATES STUDENT SCHEDULE WITH THE PREDICTION MODEL
"""

import pandas as pd


class CourseModel:
    def __init__(self):
        self.num_sem = 8
        
required_ewc = {
    "SoftDes":[False, 0],
    "SoftSys":[False,1],
    ("DSA","FoCs"):[False, 1],
    "Discrete":[False,0]
    }
required_ewc_electives = ["User Experience Design", "CompArch", "Complexity Science", "CompRobo"]

    def get_required_courses(major, study_abroad, LOA, grad_early):
        """
        Create the dataframe
        """
        sem_columns = [
            "Freshmen Fall",
            "Freshmen Spring",
            "Sophomore Fall",
            "Sophomore Spring",
            "Junior Fall",
            "Junior Spring",
            "Senior Fall",
            "Senior Spring",
        ]
        # columns=["Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6","Semester 7","Semester 8",]

        if LOA != "N/A":
            sem_columns.append("Extra Semester")

        # Initialize dataframe
        df = pd.DataFrame(None, index=range(5), columns=sem_columns)
        req_courses = {}

        if major == "E: Computing":
            # sem_courses = {
            #     "Semester 1": ["QEA1", "Modsim", "DesNat", "AHS Concentration"],
            #     "Semester 2": ["QEA2", "ISIM", "Products & Markets", "Softdes"],
            #     "Semester 3": ["PIE"],
            #     "Semester 4": ["CD"],
            #     "Semester 5": [],
            #     "Semester 6": [],
            #     "Semester 7": ["Senior Capstone"],
            #     "Semester 8": ["Senior Capstone"],
            # }
            req_courses = {
                "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS"],
                "Freshmen Spring": ["QEA2", "ISIM", "P&M", "SoftDes"],
                "Sophomore Fall": ["PIE", "Discrete", "", ""],
                "Sophomore Spring": ["CD", "SoftSys", "", ""],
                "Junior Fall": ["Bio", "MatSci", "", ""],
                "Junior Spring": ["", "", "", ""],
                "Senior Fall": ["Capstone", "", "", ""],
                "Senior Spring": ["Capstone", "", "", ""],
            }
        else:
            print("Choose a different major")
        for semester, courses in req_courses.items():
            for i, course in enumerate(courses):
                df.at[i, semester] = course

        # Blocking out the study abroad semester
        if study_abroad != "N/A":
            for i in range(len(df)):
                df.at[i, study_abroad] = "Study Abroad: AHS"
        # Blocking out the LOA semester
        if LOA != "N/A":
            for i in range(len(df)):
                df.at[i, LOA] = "LOA"
        # Blocking out graduating early
        if grad_early != "N/A":
            if grad_early == "One semester early":
                for i in range(len(df)):
                    df.at[i, "Senior Spring"] = "Already Graduated!"
            if grad_early == "One year early":
                for i in range(len(df)):
                    df.at[i, "Senior Fall"] = "Already Graduated!"
                    df.at[i, "Senior Spring"] = "Already Graduated!"

        df = df.fillna("")
        return df
