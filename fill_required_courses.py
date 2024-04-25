import pandas as pd

sem_courses = {
    "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS"],
    "Freshmen Spring": ["QEA2", "ISIM", "P&M", "SoftDes"],
    "Sophomore Fall": [
        "PIE",
        "Discrete",
    ],
    "Sophomore Spring": [
        "CD",
        "SoftSys",
    ],
    "Junior Fall": [
        "Bio",
        "MatSci",
    ],
    "Junior Spring": [],
    "Senior Fall": [
        "Capstone",
    ],
    "Senior Spring": [
        "Capstone",
    ],
}
courses_took = [
    "QEA1",
    "Modsim",
    "DesNat",
    "AHS",
    "QEA2",
    "ISIM",
    "P&M",
    "SoftDes",
    "PIE",
    "Discrete",
    "CD",
    "SoftSys",
    "Bio",
    "MatSci",
]
major_requirements = {
    "E:C": {
        "ENGR2510": [True, 0],
        "ENGR3525": [False, 1],
        "ENGR3599A/ENGR3520": [False, 1],
    },
    "MechE": {},
}
electives = {
    "E:C": ["ENGR3220", "ENGR3410", "ENGR3540", "ENGR3590", "ENGR3599"],
    "MechE": [],
}
df = pd.read_csv("predicted_schedule.csv", index_col=0).T
max_num_course = 4
major = "E:C"
last_level = 1
for courses, [took, level] in major_requirements[major].items():
    if not took:
        courses_separated = courses.split("/")
        for course in courses_separated:
            # print(f'{course}: {df[course]}')
            offering_semester_prediction = df[course].to_frame().T
            offering_semester_prediction.set_index("Course Title", inplace=True)
            offered_semesters = [
                semester
                for semester, value in offering_semester_prediction.items()
                if float(value) >= 0.5
            ]
            print(f"{course}:{offered_semesters}")
            # look through the sem_courses
            for idx, [semester, took_courses] in enumerate(sem_courses.items()):
                # skip freshman years
                if idx < 3:
                    continue
                # if a semester in sem_courses have less than max num courses
                # and is in the offered_semesters list and last_level is not higher than current level, fill it out from the start
                if (
                    semester.lower() in offered_semesters
                    and len(took_courses) < max_num_course
                    and last_level <= level
                    and course not in courses_took
                ):
                    sem_courses[semester].append(df[course]["Course Title"])
                    # change took to True
                    major_requirements[major][courses][0] = True
                    # add the course number to courses_took
                    courses_took.append(course)
                    # update level
                    last_level = level
                    continue
print(sem_courses)
