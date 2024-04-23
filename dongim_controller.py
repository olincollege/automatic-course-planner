# my_controller.py

from dongim_model import create_student_schedule
from dongim_view import render_schedule

major = "E: Computing"
study_abroad_semesters = ["Junior Spring", "Senior Fall"]
electives = [
    ((4, "Junior Fall"), ["Discrete"]),
    ((1, "Sophomore Spring"), ["ComArch", "CompRobo", "RoboSys"]),
]

schedule = create_student_schedule(major, study_abroad_semesters, electives)
render_schedule(schedule)
