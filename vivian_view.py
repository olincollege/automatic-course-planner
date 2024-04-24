import tkinter as tk
from tkinter import ttk
from pandastable import Table, TableModel
import pandas as pd
import random

from vivian_controller import CourseController

# from test_model import CourseModel


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


class CourseView:
    def __init__(self, root):
        self.root = root
        self.selected_major = ""
        self.study_abroad = ""

    def create_window(self):
        # def show_button():
        #     button.pack(padx=10, pady=10)

        # def hide_button():
        #     button.pack_forget()

        def handle_major_selection(event):
            if major_dropdown.get():
                self.selected_major = major.get()
                self.study_abroad = study_abroad.get()
            if study_abroad_dropdown.get():
                print("Selected:", self.selected_major)
                print("Study Abroad", self.study_abroad)

            if major_dropdown.get() and study_abroad_dropdown.get():
                self.selected_major = major.get()
                self.study_abroad = study_abroad.get()
                print("Selected:", self.selected_major)
                print("Study Abroad", self.study_abroad)
                # Show button
                button.pack(padx=10, pady=10)
            else:
                # Hide button
                button.pack_forget()

        # Create Tkinter root window
        # root = tk.Tk()
        self.root.title("Pandas DataFrame Viewer")
        self.root.geometry("400x300")

        # CONSTRAINTS FOR USER INPUT

        # Store selected Major
        major = tk.StringVar()
        major.set("Select a major")
        major_dropdown = ttk.Combobox(
            self.root,
            textvariable=major,
            values=[
                "E: Computing",
                "Mechanical Engineering",
                "Electrical Engineering",
                "E: Robo",
            ],
            state="readonly",
            validate="all",
        )
        major_dropdown.pack(pady=10)

        study_abroad = tk.StringVar()
        study_abroad.set("Do you plan to study abroad?")
        study_abroad_dropdown = ttk.Combobox(
            self.root,
            textvariable=study_abroad,
            values=["Yes", "No"],
            state="readonly",
            validate="all",
        )
        study_abroad_dropdown.pack(pady=10)

        # Bind the selection event of the dropdown to the handle_major_selection function
        # major_dropdown.bind(
        #     "<<ComboboxSelected>>",
        #     handle_major_selection,
        # )
        study_abroad_dropdown.bind(
            "<<ComboboxSelected>>",
            handle_major_selection,
        )

        # Initialize button
        button = ttk.Button(
            self.root,
            text="View 4 Year Course Plan",
            command=lambda: DataFrameViewer(
                self.root,
                CourseController.get_df(self.selected_major, self.study_abroad),
            ),
        )
        button.pack_forget()  # Initially hide the button

        self.root.mainloop()
