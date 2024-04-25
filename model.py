"""
UPDATED 4/23
CORRECTLY IMPLEMENTED WITH DROPDOWN AND SHOWS DATAFRAME FOR E: COMPUTING MAJOR
"""

import tkinter as tk
from tkinter import ttk
from pandastable import Table, TableModel
import pandas as pd
import random


class DataFrameViewer(tk.Toplevel):

    def __init__(self, parent, dataframe):
        # Initialize TopLevel window
        tk.Toplevel.__init__(self, parent)
        # Store regerence to parent window
        self.parent = parent
        # Set window title
        self.title("Course Schedule Viewer")

        # Create frame inside window
        self.frame = tk.Frame(self)
        # Fill window with frame
        self.frame.pack(fill="both", expand=True)

        # Create table widget with pandas dataframe
        self.table = Table(
            self.frame, dataframe=dataframe, showtoolbar=True, showstatusbar=True
        )
        self.table.show()


def calculate_credits_taken(courses_dict):
    """
    Calculate credits taken.

    Args:
        courses_dict: A dictionary with semesters as keys and lists of course numbers
            as values for each key.

    Returns:
        credits_took: A dictionary of credits taken for each area.
            eg. {'AHSE': 4, 'ENGR': 56, 'MTH/SCI': 36, 'MTH': 0, 'OFYI': 0, 'TOTAL': 96}
    """
    # Example input style
    # sem_courses = {
    #     "Freshmen Fall": ["ENGR2199B/MTH2188B", "SCI1121A/MTH2220A", "MTH2199", "AHSE1122"],
    #     "Freshmen Spring": ["SCI2210", "SCI1240", "MTH2188", "ENGX2000"],
    #     "Sophomore Fall": ["ENGX2005", "ENGX2199", "ENGR3810", "ENGR3599B"],
    #     "Sophomore Spring": ["ENGR3440", "ENGR3250", "ENGR2320", "ENGR1200"],
    #     "Junior Fall": ["ENGR3299", "SCI1230", "SCI2220", "SCI3320"],
    #     "Junior Spring": ["SUST3301", "MTH3199", "", ""],
    #     "Senior Fall": ["ENGX2199", "", "", ""],
    #     "Senior Spring": ["ENGR3640", "", "", ""],
    # }

    df = pd.read_csv("combined_schedule.csv")

    credits_took = {
        "AHSE": 0,
        "ENGR": 0,
        "MTH/SCI": 0,
        "MTH": 0,
        "SCI": 0,
        "OFYI": 0,
        "TOTAL": 0,
    }

    for courses in courses_dict.values():
        for course in courses:
            areas = course.split(
                "/"
            )  # Split course number if it contributes to multiple areas
            normalized_course_number = course.replace("/", " / ")
            for i, area in enumerate(areas):
                area_name = None
                if area.startswith("MTH"):
                    area_name = "MTH"
                elif area.startswith("SCI"):
                    area_name = "SCI"
                elif area.startswith("AHS"):
                    area_name = "AHSE"
                elif area.startswith("ENG"):
                    area_name = "ENGR"
                elif area.startswith("OFYI"):
                    area_name = "OFYI"
                if area_name and (normalized_course_number in df["Course #"].values):
                    try:
                        credits_str = df.loc[
                            df["Course #"] == normalized_course_number, "Credits"
                        ].iloc[0]
                        credits_split = credits_str.split(
                            "+"
                        )  # Split credits if multiple
                        credits_took[area_name] += int(credits_split[i])
                    except ValueError or AttributeError:
                        pass

    credits_took["TOTAL"] = sum(credits_took.values())
    credits_took["MTH/SCI"] = credits_took["MTH"] + credits_took["SCI"]
    del credits_took["SCI"]
    return credits_took


def create_student_schedule(major, study_abroad_semesters):

    sem_courses = {}

    # Define default course names
    if major == "E: Computing":
        sem_courses = {
            "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS Foundation"],
            "Freshmen Spring": ["QEA2", "ISIM", "P&M", "SoftDes"],
            "Sophomore Fall": ["PIE", "", "", ""],
            "Sophomore Spring": ["CD", "", "", ""],
            "Junior Fall": ["", "", "", ""],
            "Junior Spring": ["", "", "", ""],
            "Senior Fall": ["Capstone", "", "", ""],
            "Senior Spring": ["Capstone", "", "", ""],
        }

    elif major == "E: Robo":
        sem_courses = {
            "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS Foundation"],
            "Freshmen Spring": ["QEA2", "ISIM", "P&M", "SoftDes"],
            "Sophomore Fall": ["PIE", "QEA3", "", ""],
            "Sophomore Spring": ["CD", "", "", ""],
            "Junior Fall": ["", "", "", ""],
            "Junior Spring": ["", "", "", ""],
            "Senior Fall": ["Capstone", "", "", ""],
            "Senior Spring": ["Capstone", "", "", ""],
        }

    elif major == "Mechanical Engineering":
        sem_courses = {
            "Freshmen Fall": ["QEA1", "Modsim", "DesNat", "AHS Foundation"],
            "Freshmen Spring": ["QEA2", "ISIM", "P&M", "MechProto"],
            "Sophomore Fall": ["PIE", "QEA3", "", ""],
            "Sophomore Spring": ["CD", "", "", ""],
            "Junior Fall": ["", "", "", ""],
            "Junior Spring": ["", "", "", ""],
            "Senior Fall": ["Capstone", "", "", ""],
            "Senior Spring": ["Capstone", "", "", ""],
        }

    # Change index name to "Study Abroad" for specified semesters
    for semester in study_abroad_semesters:
        sem_courses[f"{semester} (Study Abroad)"] = sem_courses.pop(semester)

    # Create an empty DataFrame with 4 rows and 8 columns
    data = pd.DataFrame(index=range(1, 5), columns=sem_courses.keys())

    # Fill in course names for each semester
    for col, courses in zip(sem_courses.keys(), sem_courses.values()):
        data[col] = courses

    return data


def main():
    def show_button():
        button.pack(padx=10, pady=10)

    def hide_button():
        button.pack_forget()

    def handle_major_selection(event):
        selected_major = major.get()
        print("Selected:", selected_major)
        if selected_major:
            show_button()
        else:
            hide_button()

    def get_df():
        return create_student_schedule(major.get(), ["Junior Spring", "Senior Fall"])

    # Create Tkinter root window
    root = tk.Tk()
    root.title("Pandas DataFrame Viewer")
    root.geometry("400x300")

    # Store selected Major
    major = tk.StringVar()
    major.set("Select a major")

    # Create a list of options for the dropdown
    major_dropdown = ttk.Combobox(
        root,
        textvariable=major,
        values=[
            "E: Computing",
            "Mechanical Engineering",
            "E: Robo",
        ],
    )
    major_dropdown.pack(pady=10)

    # Initialize button
    button = ttk.Button(
        root,
        text="View DataFrame",
        command=lambda: DataFrameViewer(root, get_df()),
    )
    # print("the major is", major.get)

    # Bind the selection event of the dropdown to the handle_major_selection function
    major_dropdown.bind("<<ComboboxSelected>>", handle_major_selection)

    root.mainloop()


if __name__ == "__main__":
    main()
