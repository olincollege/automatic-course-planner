"""
UPDATED 4/23
CORRECTLY IMPLEMENTED WITH DROPDOWN AND SHOWS DATAFRAME FOR E: COMPUTING MAJOR
"""

import tkinter as tk
from tkinter import ttk
from pandastable import Table, TableModel
import pandas as pd


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


def get_required(major):
    columns = [
        "Semester 1",
        "Semester 2",
        "Semester 3",
        "Semester 4",
        "Semester 5",
        "Semester 6",
        "Semester 7",
        "Semester 8",
    ]
    df = pd.DataFrame(None, index=range(5), columns=columns)

    sem_courses = {}

    # Required Courses for E:C
    if major == "E: Computing":
        # electives = {"FoCS": "90%", "Discrete": "10%", "CompRobo": "50%"}
        sem_courses = {
            "Semester 1": ["QEA1", "Modsim", "DesNat", "AHS Concentration"],
            "Semester 2": ["QEA2", "ISIM", "Products & Markets", "Softdes"],
            "Semester 3": ["PIE", "Discrete"],
            "Semester 4": ["CD", "SoftSys"],
            "Semester 5": ["Bio", "MatSci"],
            "Semester 6": [],
            "Semester 7": ["Senior Capstone"],
            "Semester 8": ["Senior Capstone"],
        }
    else:
        print("No courses for selected major")
    # Loop through the dictionary and assign courses to DataFrame
    for semester, courses in sem_courses.items():
        for i, course in enumerate(courses):
            df.at[i, semester] = course
    df = df.fillna("")
    return df


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
        return get_required(major.get())

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
