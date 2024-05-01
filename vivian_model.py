"""
CREATES STUDENT SCHEDULE WITH THE PREDICTION MODEL
"""

import pandas as pd
import numpy as np
import random

import warnings

# # Settings the warnings to be ignored
warnings.filterwarnings("ignore")


class CourseModel:
    """
    All the logic behind the dataframe
    """

    def __init__(self, major, loa, study_abroad, grad_early):
        """
        initilize everything in self

        Args:
            major: a string representing user input of selected major
            LOA: a string representing user input of LOA semester
            study_abroad: a string represtiing user input of study abraod semester
            grad_early: a string representing user input of graduating early
        """

        self.courses_list_remove = {
            "freshman fall": [],
            "freshman spring": [],
            "sophomore fall": [],
            "sophomore spring": [],
            "junior fall": [],
            "junior spring": [],
            "senior fall": [],
            "senior spring": [],
        }
        # User inputs
        self.major = major
        self.study_abroad = study_abroad
        self.loa = loa
        self.grad_early = grad_early

        self.MAX_COURSES = 4
        self.df_transposed = pd.read_csv("predicted_schedule.csv", index_col=0).T
        self.df = pd.read_csv("predicted_schedule.csv", index_col=0)

        # Initialize empty dataframe
        # self.df = pd.DataFrame(
        #     "",
        #     index=range(self.MAX_COURSES),
        #     columns=[
        #         "Freshmen Fall",
        #         "Freshmen Spring",
        #         "Sophomore Fall",
        #         "Sophomore Spring",
        #         "Junior Fall",
        #         "Junior Spring",
        #         "Senior Fall",
        #         "Senior Spring",
        #     ],
        # )
        self.sem_courses = {
            "freshmen fall": ["QEA1", "Modsim", "DesNat", "AHS"],
            "freshmen spring": [
                "QEA2",
                "ISIM",
                "P&M",
            ],
            "sophomore fall": [
                "PIE",
            ],
            "sophomore spring": [
                "CD",
            ],
            "junior fall": [],
            "junior spring": [],
            "senior fall": ["Capstone"],
            "senior spring": [
                "Capstone",
            ],
        }
        self.emtpy_sem_courses = {}

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

        self.credits_needed = {  # should not change
            "AHS": 28 - 8,
            "ENG": 46 - 24,
            "MTH/SCI": 30 - 4,
            "MTH": 10 - 4,
            "SCI": 0,
            "OFYI": 1,
            "TOTAL": 120 - 37,
        }
        self.credits_took = {
            "AHS": 8,
            "ENG": 24,
            "MTH/SCI": 4,
            "MTH": 4,
            "SCI": 0,
            "OFYI": 1,
            "TOTAL": 37,
        }

        # Constraints -- based on major
        # self.required_courses = {}  # {"Semester": [course1, course2]}

        self.major_requirements = {
            "E: Computing": {
                "ENGR2510": [True, 0],
                "ENGR3525": [False, 1],
                "ENGR3599A/ENGR3520": [False, 1],
                "ENGR3220/ENGR3410/ENGR3540": [False, 1],
                "ENGR3590/ENGR3599": [False, 1],
            },
            "Electrical Engineering": {
                "ENGX2010": [False, 0],
                "ENGR2510": [True, 0],
                "ENGX2134": [False, 1],
                "ENGR2410": [False, 1],
                "ENGR2420": [False, 1],
                "ENGR2199B": [False, 1],
                "ENGR3410": [False, 1],
                "ENGR3110": [False, 2],
                "ENGR3370": [False, 2],
                "ENGR3390": [False, 1],
                "ENGR3392": [False, 2],
                "ENGR3415": [False, 2],
                "ENGR3420": [False, 2],
                "ENGR3426": [False, 2],
                "ENGR3430": [False, 3],
                "ENGR3440": [False, 3],
                "ENGR3499": [False, 2],
                "MTH2110": [False, 0],
            },
            "Mechanical Engineering": {
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
        self.other_requirements = {
            "bio_requirements": [
                "ENGR3235/SCI2235",
                "SCI1250/AHSE2150",
                "SCI1260/AHSE2160",
                "SCI1270",
                "SCI1299",
                "SCI2214",
                "SCI1230",
                "SCI2299",
            ],
            "design_depth_requirements": [
                "ENGR3220",
                "ENGR3260",
                "ENGR3299",
                "ENGR3299A",
                "ENGR3235/SCI2235",
                "AHSE2199/ENGR2299",
                "ENGR3252",
                "ENGR3210",
            ],
            "probstat_requirements": [
                "MTH2135/ENGR3635",
                "MTH2136/SCI2136",
                "MTH2130",
                "ENGR3531/MTH2131",
                "MTH2188A/ENGR3599A",
                "ENGR3533/MTH2133",
            ],
            "matsci_requirements": ["SCI1320", "SCI1410", "SCI1440", "SCI1420"],
        }

        self.other_requirements_fulfilled = {
            "bio_requirements": False,
            "design_depth_requirements": False,
            "probstat_requirements": False,
            "matsci_requirements": False,
        }

    # USER CONSTRAINED METHODS
    def fill_major_required_courses(self):
        """
        Create and fill the dataframe with required courses.
        This should be dependent on major
        """
        LAST_LEVEL = 0

        for courses, [took, level] in self.major_requirements[self.major].items():
            courses_separated = courses.split("/")
            for course in courses_separated:
                offering_semester_prediction = self.df_transposed[course].to_frame().T
                offering_semester_prediction.set_index("Course Title", inplace=True)
                offered_semesters = [
                    semester
                    for semester, value in offering_semester_prediction.items()
                    if float(value) >= 0.5
                ]
                course_title = self.df_transposed[course]["Course Title"]

                # look through the sem_courses
                for idx, [semester, took_courses] in enumerate(
                    self.sem_courses.items()
                ):
                    if (
                        semester.lower() in offered_semesters
                        and len(took_courses) < self.MAX_COURSES
                        and LAST_LEVEL <= level
                        and course not in self.courses_took
                        and self.major_requirements[self.major][courses][0] is False
                    ):
                        # fill in course to sem_courses
                        self.sem_courses[semester].append(course_title)
                        # change took to True
                        self.major_requirements[self.major][courses][0] = True
                        # add the course number to courses_took
                        self.courses_took.append(course)
                        # update credits needed
                        self.credits_needed[course[:3]] -= 4
                        self.credits_needed["TOTAL"] -= 4
                        # update level
                        LAST_LEVEL = level
                        break

    def fill_loa(self):
        """
        Fill dataframe with blocked out spots of when
        user is taking an LOA
        """
        if self.loa != "N/A":
            # Add an extra row if someone is taking an LOA
            self.MAX_COURSES = 5
            empty_row_data = [np.nan] * len(
                self.df_transposed.columns
            )  # Create a list of NaN values
            self.df_transposed.loc[len(self.df_transposed)] = empty_row_data

            # Blocking out the LOA semester
            self.sem_courses[self.loa] = ["LOA"] * self.MAX_COURSES

    def fill_study_abroad(self):
        """
        Fill dataframe with blocked out spots of when
        user is studying abroad
        """
        # Blocking out the study abroad semester
        if self.study_abroad != "N/A":
            self.sem_courses[self.study_abroad] = [
                "Study Abroad: AHS"
            ] * self.MAX_COURSES
            self.credits_needed["AHS"] -= 12
            self.credits_needed["TOTAL"] -= 12

    def fill_grad_early(self):
        """
        Fill dataframe with blocked out spots of if
        user is graduating early
        """
        # Blocking out graduating early
        if self.grad_early != "N/A":
            if self.grad_early == "One semester early":
                self.MAX_COURSES = 5
                self.sem_courses["senior spring"] = [
                    "Graduating Early!"
                ] * self.MAX_COURSES

            if self.grad_early == "One year early":
                self.MAX_COURSES = 5
                self.sem_courses["senior spring"] = [
                    "Graduating Early!"
                ] * self.MAX_COURSES
                self.sem_courses["senior fall"] = [
                    "Graduating Early!"
                ] * self.MAX_COURSES

    # HELPER METHODS

    def get_course_type(self, course):
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

    def get_possible_courses(self, semester):
        """
        Get possible course for each semester as a dictionary along with its likelihood of offering
        Args:
            semester(str): semester that you want to check the course offering for (e.g., 'freshmen fall')
            df (DataFrame): DataFrame containing the course offering data
        Returns:
            course offering dictionary with likelihood, separated by course type
        """
        # Initialize an empty dictionary to store offered courses by type
        offered_courses = {"MTH": {}, "ENG": {}, "SCI": {}, "AHS": {}}
        # Find the corresponding column index for the semester
        semester_column = semester.lower()
        # Check if the semester column exists in the DataFrame
        if semester_column in self.df.columns:
            # Filter the DataFrame for courses offered in the specified semester with values greater than 0.5
            courses_offered = self.df[self.df[semester_column] > 0.5]
            # Iterate through the courses offered and categorize them by type
            for course in courses_offered.index.tolist():
                course_type = self.get_course_type(course)
                if course_type:
                    offered_courses[course_type][course] = courses_offered.loc[
                        course, semester_column
                    ]

        return offered_courses

    def get_possible_semesters(self, course_number):
        """
        Extracts semesters with a likelihood greater than 0.5 for a given course number ordered by likelihood.

        Args:
            df (DataFrame): DataFrame containing the likelihood of the course being offered for different semesters.
            course_number (str): The course number for which semesters are to be extracted.

        Returns:
            list: An ordered list of semesters with likelihood greater than 0.5 for the given course number.
        """
        # Remove the first element (Course Title) from the row and make it into DataFrame
        possible_semesters_df = pd.DataFrame(self.df_transposed[course_number][1:])

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

    # OTHER METHODS

    def calculate_credits_taken(self):
        """
        Udpate the dictionary of credits taken
        """
        for course in self.courses_took:
            course_type = self.get_course_type(course)
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
        # self.fill_major_required_courses()
        # for semester, courses in self.required_courses.items():
        #     self.empty_sem_courses[semester] = courses.count("")
        for semester, courses in self.sem_courses.items():
            self.emtpy_sem_courses[semester] = courses.count("")
        return self.emtpy_sem_courses

    def fill_other_requirements(self):
        for (
            course_type,
            courses,
        ) in self.other_requirements.items():  # courses is list of course number
            for course in courses:
                # among the semester the course would be offered,
                possible_semesters = self.get_possible_semesters(course)
                for semester in possible_semesters:
                    # if the person is taking less courses than MAX_COURSES in the semester
                    if (
                        len(self.sem_courses[semester]) < self.MAX_COURSES
                        and not self.other_requirements_fulfilled[course_type]
                    ):
                        # fill in the sem_courses
                        course_title = self.df_transposed[course]["Course Title"]
                        self.sem_courses[semester].append(course_title)
                        # add it to the courses_took
                        self.courses_took.append(course)
                        # update credits needed
                        self.credits_needed[course[:3]] -= 4
                        self.credits_needed["TOTAL"] -= 4
                        self.other_requirements_fulfilled[course_type] = True
                        break
        # return self.sem_courses

    # HELPER FUNCTION
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
            possible_courses = self.get_possible_courses(semester)
            all_possible_courses = {}
            for courses in possible_courses.values():
                all_possible_courses.update(courses)

            possible_courses = all_possible_courses
        else:  # if there is a choosen course type
            possible_courses = self.get_possible_courses(semester)[course_type]
        # Extract course names and their weights
        course_names = list(possible_courses.keys())
        weights = list(possible_courses.values())
        # Randomly choose a course based on weights

        # for course in self.courses_list_remove[semester]:
        #     if course in course_names:
        #         index = course_names.index(course)
        #         course_names.remove(course)
        #         weights.pop(index)

        chosen_course = random.choices(course_names, weights=weights)[0]

        # self.courses_list_remove[semester].append(chosen_course)

        # course_names.remove(chosen_course)
        # if the chosen course is in the courses took, choose another course
        # while chosen_course in self.courses_took:
        #     chosen_course = random.choices(course_names, weights=weights)[0]
        #     print("chosen course", chosen_course)
        #     print(self.courses_took)
        #     print()
        return chosen_course

    def fill_empty_schedules(self):
        """
        Fill courses in semesters based on major requirements, course offerings, and credit requirements.
        """
        print("ITS WORKING 1")
        while self.credits_needed["TOTAL"] > 0:
            print(self.credits_needed)
            # fill MTH if not enough math credit
            if self.credits_needed["MTH"] > 0:
                print("mathcredits", self.credits_needed["MTH"])
                for semester, courses in self.sem_courses.items():
                    if len(courses) < self.MAX_COURSES:
                        print(semester)
                        choosen_course = self.choose_course(  # not transposed df
                            semester, "MTH"
                        )  # course num
                        print(choosen_course)
                        choosen_course_title = self.df_transposed[
                            choosen_course
                        ][  # transposed df
                            "Course Title"
                        ]  # course title
                        self.sem_courses[semester].append(choosen_course_title)
                        self.courses_took.append(choosen_course)
                        self.credits_needed["MTH"] -= 4
                        self.credits_needed["MTH/SCI"] -= 4
                        self.credits_needed["TOTAL"] -= 4
                        print(self.credits_needed)
                        break
            # fill MTH/SCI

            elif self.credits_needed["MTH/SCI"] > 0:
                print("Goes to mth/sci")
                for semester, courses in self.sem_courses.items():
                    print(semester)
                    if len(courses) < self.MAX_COURSES:
                        # if MTH/SCI just fill in with SCI courses??
                        choosen_course = self.choose_course(
                            semester, "SCI"
                        )  # course num
                        choosen_course_title = self.df_transposed[choosen_course][
                            "Course Title"
                        ]  # course title
                        self.sem_courses[semester].append(choosen_course_title)
                        self.courses_took.append(choosen_course)
                        print(self.credits_needed["MTH/SCI"])
                        self.credits_needed["MTH/SCI"] -= 4
                        self.credits_needed["TOTAL"] -= 4

            # fill ENG
            elif self.credits_needed["ENG"] > 0:
                print("Goes to eng")
                for semester, courses in self.sem_courses.items():
                    print(semester)
                    if len(courses) < self.MAX_COURSES:
                        print(len(courses))
                        choosen_course = self.choose_course(
                            semester, "ENG"
                        )  # course num
                        print(choosen_course)
                        choosen_course_title = self.df_transposed[choosen_course][
                            "Course Title"
                        ]  # course title
                        self.sem_courses[semester].append(choosen_course_title)
                        self.courses_took.append(choosen_course)
                        self.credits_needed["ENG"] -= 4
                        self.credits_needed["TOTAL"] -= 4
                        print(self.credits_needed)

            # fill AHS --> just 'AHS', no calculation
            elif self.credits_needed["AHS"] > 0:
                print("Goes to ahs")
                for semester, courses in self.sem_courses.items():
                    if len(courses) < self.MAX_COURSES:
                        self.sem_courses[semester].append("AHS")
                        self.courses_took.append("AHS")
                        self.credits_needed["AHS"] -= 4
                        self.credits_needed["TOTAL"] -= 4

            # fill TOTAL with any course
            else:
                print("Goes to total")
                for semester, courses in self.sem_courses.items():
                    if len(courses) < self.MAX_COURSES:
                        choosen_course = self.choose_course(semester)  # course num
                        choosen_course_title = self.df_transposed[choosen_course][
                            "Course Title"
                        ]  # course title
                        self.sem_courses[semester].append(choosen_course_title)
                        self.courses_took.append(choosen_course)
                        self.credits_needed[choosen_course[0:3]] -= 4  # course type
                        self.credits_needed["TOTAL"] -= 4

        # return self.sem_courses
        print(self.sem_courses)

    def get_df(self):
        """
        CALL ALL THE OTHER FUNCTIONS TO FILL DF BEFORE RETURNING

        """
        max_length = max(len(lst) for lst in self.sem_courses.values())
        for key, value in self.sem_courses.items():
            while len(value) < max_length:
                value.append("")
        filled_df = pd.DataFrame(self.sem_courses)
        return filled_df


# coursemodel = CourseModel("E:Computing", "junior fall", "N/A", "N/A")
# coursemodel.fill_loa()

# print(coursemodel.sem_courses)
