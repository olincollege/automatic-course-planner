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
            ["FoCS", "CompRobo"], weights=(50, 50)
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


def main():
    def show_button():
        button.pack(padx=10, pady=10)

    def hide_button():
        button.pack_forget()

    def handle_major_selection(event):
        selected_major = major.get()
        print("Selected:", selected_major)
        if selected_major == "E: Computing":
            show_button()
        else:
            hide_button()

    def get_df():
        electives = [
            ((4, "Junior Fall"), ["Discrete"]),
            ((1, "Sophomore Spring"), ["ComArch", "CompRobo", "RoboSys"]),
        ]
        return create_student_schedule(
            major.get(), ["Junior Spring", "Senior Fall"], electives
        )

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
            "Electrical Engineering",
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
