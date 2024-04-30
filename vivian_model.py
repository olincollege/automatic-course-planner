"""
CREATES STUDENT SCHEDULE WITH THE PREDICTION MODEL
"""

import pandas as pd
import numpy as np
import random
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

        self.MAX_COURSES = 4

        # Initialize empty dataframe
        self.df = pd.DataFrame(
            "",
            index=range(self.MAX_COURSES),
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
        self.courses_took = [
            "MTH1111/SCI1111",  # ModSim
            "ENGR1200",  # DesNat
            "AHSE0112",  # OCO
            "ENGX2005",  # QEA 2
            "ENGR1125",  # ISIM
            "AHSE1515",  # P&M
            "ENGR2110",  # PIE
            "ENGR2250",  # CD
        ]

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

    # USER CONSTRAINED METHODS
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

    def fill_loa(self):
        """
        Fill dataframe with blocked out spots of when
        user is taking an LOA
        """
        # Add an extra row if someone is taking an LOA
        self.MAX_COURSES = 5
        empty_row_data = [np.nan] * len(self.df.columns)  # Create a list of NaN values
        self.df.loc[len(self.df)] = empty_row_data

        # Blocking out the LOA semester
        if self.loa != "N/A":
            for i in range(len(self.df)):
                self.df.at[i, self.loa] = "LOA"

    def fill_study_abroad(self):
        """
        Fill dataframe with blocked out spots of when
        user is studying abroad
        """
        # Blocking out the study abroad semester
        if self.study_abroad != "N/A":
            for i in range(len(self.df)):
                self.df.at[i, self.study_abroad] = "Study Abroad: AHS"

    def fill_grad_early(self):
        """
        Fill dataframe with blocked out spots of if
        user is graduating early
        """
        # Blocking out graduating early
        if self.grad_early != "N/A":
            if self.grad_early == "One semester early":
                for i in range(len(self.df)):
                    self.df.iloc[i, -1] = "Already Graduated!"
            if self.grad_early == "One year early":
                for i in range(len(self.df)):
                    self.df.iloc[i, -2] = "Already Graduated!"
                    self.df.iloc[i, -1] = "Already Graduated!"

    # OTHER METHODS

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
                    self.credits_took["MTH/SCI"] += 4
                self.credits_took[course_type] += 4
                self.credits_took["TOTAL"] += 4

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
        # CHECK UPDATED
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
                        len(self.required_courses[semester]) < self.MAX_COURSES
                        and not self.other_requirements_fulfilled[course_type]
                    ):
                        # fill in the sem_courses
                        course_title = self.df[course]["Course Title"]
                        self.required_courses[semester].append(course_title)
                        # add it to the courses_took
                        self.courses_took.append(course)
                        self.other_requirements_fulfilled[course_type] = True
                        break

    def choose_course(self, semester, course_type="ALL"):
        """
        choose a course for the course_type and semester according to its liklihood of offering
        if course_type is ALL, choose from any subject

        Args:
        course_type:
        semester:

        return:
            course num
        """
        if course_type == "ALL":
            possible_courses = get_possible_courses(semester, df)
            all_possible_courses = {}
            for courses in possible_courses.values():
                all_possible_courses.update(courses)

            possible_courses = all_possible_courses
            print(possible_courses)
        else:  # if there is a choosen course type
            possible_courses = get_possible_courses(semester, df)[course_type]
        # Extract course names and their weights
        course_names = list(possible_courses.keys())
        weights = list(possible_courses.values())

        # Randomly choose a course based on weights
        random_course = random.choices(course_names, weights=weights)[0]
        return random_course

    def fill_empty_schedules(sem_courses):
        """
        Fill courses in semesters based on major requirements, course offerings, and credit requirements.
        """

        while credits_needed["TOTAL"] > 0:
            # fill MTH if not enough math credit
            if credits_needed["MTH"] > 0:
                for semester, courses in sem_courses.items():
                    if len(courses) < MAX_NUM_COURSE:
                        choosen_course = choose_course(semester, "MTH")  # course num
                        choosen_course_title = df.T[choosen_course][
                            "Course Title"
                        ]  # course title
                        sem_courses[semester].append(choosen_course_title)
                        courses_took.append(choosen_course)
                        credits_needed["MTH"] -= 4
                        credits_needed["MTH/SCI"] -= 4
                        credits_needed["TOTAL"] -= 4
            # fill MTH/SCI
            elif credits_needed["MTH/SCI"] > 0:
                for semester, courses in sem_courses.items():
                    if len(courses) < MAX_NUM_COURSE:
                        # if MTH/SCI just fill in with SCI courses??
                        choosen_course = choose_course(semester, "SCI")  # course num
                        choosen_course_title = df.T[choosen_course][
                            "Course Title"
                        ]  # course title
                        sem_courses[semester].append(choosen_course_title)
                        courses_took.append(choosen_course)
                        credits_needed["SCI"] -= 4
                        credits_needed["MTH/SCI"] -= 4
                        credits_needed["TOTAL"] -= 4
            # fill ENG
            elif credits_needed["ENG"] > 0:
                for semester, courses in sem_courses.items():
                    if len(courses) < MAX_NUM_COURSE:
                        choosen_course = choose_course(semester, "SCI")  # course num
                        choosen_course_title = df.T[choosen_course][
                            "Course Title"
                        ]  # course title
                        sem_courses[semester].append(choosen_course_title)
                        courses_took.append(choosen_course)
                        credits_needed["ENG"] -= 4
                        credits_needed["TOTAL"] -= 4
            # fill AHS --> just 'AHS', no calculation
            elif credits_needed["AHS"] > 0:
                for semester, courses in sem_courses.items():
                    if len(courses) < MAX_NUM_COURSE:
                        sem_courses[semester].append("AHS")
                        courses_took.append("AHS")
                        credits_needed["AHS"] -= 4
                        credits_needed["TOTAL"] -= 4
            # fill TOTAL with any course
            else:
                for semester, courses in sem_courses.items():
                    if len(courses) < MAX_NUM_COURSE:
                        choosen_course = choose_course(semester)  # course num
                        choosen_course_title = df.T[choosen_course][
                            "Course Title"
                        ]  # course title
                        sem_courses[semester].append(choosen_course_title)
                        courses_took.append(choosen_course)
                        credits_needed[choosen_course[0:3]] -= 4  # course type
                        credits_needed["TOTAL"] -= 4
        return sem_courses

    def get_df(self):
        """
        CALL ALL THE OTHER FUNCTIONS TO FILL DF BEFORE RETURNING

        """
        return self.df
