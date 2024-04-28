import pandas as pd
import warnings

# Settings the warnings to be ignored
warnings.filterwarnings("ignore")


sem_courses = {
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
courses_took = [
    "ENGX2000",  # QEA
    "MTH1111/SCI1111",  # ModSim
    "ENGR1200",  # DesNat
    "AHSE0112",  # OCO
    "ENGX2005",  # QEA 2
    "ENGR1125",  # ISIM
    "AHSE1515",  # P&M
    "ENGR2110",  # PIE
    "ENGR2250",  # CD
]
major_requirements = {
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

df = pd.read_csv("predicted_schedule.csv", index_col=0).T
MAX_NUM_COURSE = 4
MAJOR = "E:C"
LAST_LEVEL = 0
for courses, [took, level] in major_requirements[MAJOR].items():
    courses_separated = courses.split("/")
    for course in courses_separated:
        offering_semester_prediction = df[course].to_frame().T
        offering_semester_prediction.set_index("Course Title", inplace=True)
        offered_semesters = [
            semester
            for semester, value in offering_semester_prediction.items()
            if float(value) >= 0.5
        ]
        course_title = df[course]["Course Title"]
        print(course_title, offering_semester_prediction)

        print(f"{course_title}:{offered_semesters}")
        # look through the sem_courses
        for idx, [semester, took_courses] in enumerate(sem_courses.items()):
            if (
                semester.lower() in offered_semesters
                and len(took_courses) < MAX_NUM_COURSE
                and LAST_LEVEL <= level
                and course not in courses_took
                and major_requirements[MAJOR][courses][0] is False
            ):
                # fill in course to sem_courses
                sem_courses[semester].append(course_title)
                # change took to True
                major_requirements[MAJOR][courses][0] = True
                # add the course number to courses_took
                courses_took.append(course)
                # update level
                LAST_LEVEL = level
                break

print(sem_courses)
print(courses_took)

b = {
    "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS"],
    "Freshmen Spring": [
        "QEA2",
        "ISIM",
        "P&M",
    ],
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

a = {
    "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS"],
    "Freshmen Spring": ["QEA2", "ISIM", "P&M"],
    "Sophomore Fall": [
        "PIE",
        "ENGX2010: Quantitative Engineering Analysis 3",
        "ENGX2134: Engineering Systems Analysis (2cr)",
        "ENGR2360: Introduction to Thermal-Fluid Systems",
    ],
    "Sophomore Spring": [
        "CD",
        "Mechanics of Solids and Structures",
        "ENGR2340: Dynamics",
        "MTH3120: Partial Differential Equations",
    ],
    "Junior Fall": ["Mechanical Design", "Design for Manufacturing"],
    "Junior Spring": [],
    "Senior Fall": ["Capstone"],
    "Senior Spring": ["Capstone"],
}
{
    "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS"],
    "Freshmen Spring": ["QEA2", "ISIM", "P&M"],
    "Sophomore Fall": [
        "PIE",
        "Human Factors Interface Design",
        "Special Topics in Computing: Computer Networks",
    ],
    "Sophomore Spring": [
        "CD",
        "Software Design",
        "ENGR3525: Software Systems",
        "ENGR3599A: Special Topics in Computing: Data Structures Algorithms",
    ],
    "Junior Fall": [],
    "Junior Spring": [],
    "Senior Fall": ["Capstone"],
    "Senior Spring": ["Capstone"],
}
