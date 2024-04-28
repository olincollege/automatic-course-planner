"""
CREATES STUDENT SCHEDULE WITH THE PREDICTION MODEL
"""

import pandas as pd
from course_planner_helper import (
    get_course_type,
    get_possible_courses,
    get_possible_semesters,
)


class CourseModel:
    """
    All the logic behind the dataframe
    """

    def __init__(self, major, study_abroad, loa, grad_early):
        """
        initilize everything in self

        Args:
            major: a string representing user input of selected major
            study_abroad: a string represtiing user input of study abraod semester
            LOA: a string representing user input of LOA semester
            grad_early: a string representing user input of graduating early
        """

        # User inputs
        self.major = major
        self.study_abroad = study_abroad
        self.loa = loa
        self.grad_early = grad_early

        # To adjust later on
        # self.num_sem = 8
        # self.sem_columns = self.columns

        # Initialize empty dataframe
        self.df = pd.DataFrame(
            "",
            index=range(5),
            columns=[
                "Freshmen Fall",
                "Freshmen Spring",
                "Sophomore Fall",
                "Sophomore Spring",
                "Junior Fall",
                "Junior Spring",
                "Senior Fall",
                "Senior Spring",
            ],
        )
        self.empty_sem_courses = {}

        # Courses taken
        self.courses_took = []

        self.TOTAL_CREDITS_REQUIRED = {  # should not change
            "AHSE": 28,
            "ENGR": 46,
            "MTH/SCI": 30,
            "MTH": 10,
            "OFYI": 1,
            "TOTAL": 120,
        }
        self.credits_took = {
            "AHSE": 0,
            "ENGR": 0,
            "MTH/SCI": 0,
            "MTH": 0,
            "SCI": 0,
            "OFYI": 0,
            "TOTAL": 0,
        }
        self.credits_left = {
            "AHSE": 0,
            "ENGR": 0,
            "MTH/SCI": 0,
            "MTH": 0,
            "SCI": 0,
            "OFYI": 0,
            "TOTAL": 0,
        }

        # Constraints -- based on major
        self.required_courses = {}  # {"Semester": [course1, course2]}

        self.major_requirements = {
            "E:C": {
                "ENGR2510": [True, 0],
                "ENGR3525": [False, 1],
                "ENGR3599A/ENGR3520": [False, 1],
                "ENGR3220/ENGR3410/ENGR3540": [False, 1],
                "ENGR3590/ENGR3599": [False, 1],
            },
            "MechE": {
                "ENGX2010": [False, 0],
                "ENGR2320": [False, 0],
                "ENGX2134": [False, 0],
                "ENGR2340": [False, 1],
                "ENGR2360": [False, 1],
                "ENGR3330": [False, 1],
                "ENGR3110/ENGR3180/ENGR3232/ENGR3299C/ENGR3260/ENGR3345/ENGR3350/ENGR3370/ENGR3392/ENGR3820": [
                    False,
                    1,
                ],
                "MTH3120/MTH3150/MTH3170": [False, 1],
            },
        }

        # Requirements
        # self.bio_requirements = []
        # self.design_depth_requirements = []
        # self.probstat_requirements = []
        # self.matsci_requirements = []
        self.other_requirements = {
            "bio": ["SCI1270", "SCI1260/AHSE2160"],
            "design_depth": ["ENGR3210", "ENGR3290", "ENGR3250"],
            "probstat": [
                "MTH2130",
            ],
            "matsci": ["SCI1440"],
        }
        self.other_requirements_fulfilled = {
            "bio": False,
            "design_depth": False,
            "probstat": False,
            "matsci": False,
        }

    def fill_major_required_courses(self):
        """
        Create and fill the dataframe with required courses.
        This should be dependent on major
        """

        if self.major == "E: Computing":
            self.required_courses = {
                "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS"],
                "Freshmen Spring": ["QEA2", "ISIM", "P&M", "Softdes"],
                "Sophomore Fall": [
                    "PIE",
                ],
                "Sophomore Spring": [
                    "CD",
                ],
                "Junior Fall": [],
                "Junior Spring": [],
                "Senior Fall": [
                    "Capstone",
                ],
                "Senior Spring": [
                    "Capstone",
                ],
            }
        elif self.major == "Mechanical Engineering":
            pass
        else:
            print("Choose a different major")

        # Fill dataframe
        for semester, courses in self.required_courses.items():
            for i, course in enumerate(courses):
                self.df.at[i, semester] = course

    def fill_study_abroad(self):
        """
        Fill dataframe with blocked out spots of when
        user is studying abroad
        """
        # Blocking out the study abroad semester
        if self.study_abroad != "N/A":
            for i in range(len(self.df)):
                self.df.at[i, self.study_abroad] = "Study Abroad: AHS"

    def fill_loa(self):
        """
        Fill dataframe with blocked out spots of when
        user is taking an LOA
        """
        # Blocking out the LOA semester
        if self.loa != "N/A":
            for i in range(len(self.df)):
                self.df.at[i, self.loa] = "LOA"
        # Add an extra semester
        self.df["Extra Sem"] = ""

    def fill_grad_early(self):
        """
        Fill dataframe with blocked out spots of if
        user is graduating early
        """
        # Blocking out graduating early
        if self.grad_early != "N/A":
            if self.grad_early == "One semester early":
                for i in range(len(self.df)):
                    self.df.at[i, "Senior Spring"] = "Already Graduated!"
            if self.grad_early == "One year early":
                for i in range(len(self.df)):
                    self.df.at[i, "Senior Fall"] = "Already Graduated!"
                    self.df.at[i, "Senior Spring"] = "Already Graduated!"

    def list_courses_took(self):
        """
        Update list of courses taken
        """
        # NEED TO FIX IT SO THAT WHENEVER THIS IS CALLED IT DOESNT
        # KEEP ADDING ON TO IT, WHICH MEANS REPEATS
        for column in self.df.columns:
            for course in self.df[column]:
                # Check if the value is not empty
                if course != "":
                    self.courses_took.append(course)

    def calculate_credits_taken(self):
        """
        Udpate the dictionary of credits taken
        """
        self.list_courses_took()

        for course in self.courses_took:
            course_type = get_course_type(course)
            if course_type:
                # If the course type is valid, add the corresponding credits
                if course_type == "MTH" or "SCI":
                    self.credits_took["MTH/SCI"] += 1
                self.credits_took[course_type] += 1
                self.credits_took["TOTAL"] += 1

    def calculate_credits_left(self):
        """
        Subtract TOTAL_CREDITS_REQUIRED - credits taken
        """
        self.calculate_credits_taken()

        self.credits_left = {
            key: self.TOTAL_CREDITS_REQUIRED[key] - self.credits_took[key]
            for key in self.TOTAL_CREDITS_REQUIRED
        }

    def get_empty_schedules(self):
        """
        get empty schedules from sem_courses
        Return:
            dictionary of how many course are free(should be filled in) for each semester.
        """
        self.fill_major_required_courses()
        for semester, courses in self.required_courses.items():
            self.empty_sem_courses[semester] = courses.count("")

    def fill_other_requirements(self):
        MAX_COURSES = 4
        for (
            course_type,
            courses,
        ) in self.other_requirements.items():  # courses is list of course number
            for course in courses:
                # among the semester the course would be offered,
                possible_semesters = get_possible_semesters(course)
                for semester in possible_semesters:
                    # if the person is taking less courses than MAX_COURSES in the semester
                    if (
                        len(self.required_courses[semester]) < MAX_COURSES
                        and not self.other_requirements_fulfilled[course_type]
                    ):
                        # fill in the sem_courses
                        course_title = self.df[course]["Course Title"]
                        self.required_courses[semester].append(course_title)
                        # add it to the courses_took
                        self.courses_took.append(course)
                        self.other_requirements_fulfilled[course_type] = True
                        break

    def get_df(self):
        """
        CALL ALL THE OTHER FUNCTIONS TO FILL DF BEFORE RETURNING

        """
        return self.df
