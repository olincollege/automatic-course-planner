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
        self.LOA = ""
        self.grad_early = ""

    def create_window(self):
        """
        Show and run the event of getting user input
        """

        def handle_major_selection(event):
            # if major_dropdown.get():
            #     self.selected_major = major.get()
            #     print("Selected:", self.selected_major)

            # if study_abroad_dropdown.get():
            #     self.study_abroad = study_abroad.get()
            #     print("Study Abroad", self.study_abroad)

            if (
                major_dropdown.get()
                and study_abroad_dropdown.get()
                and LOA_dropdown.get()
                and grad_early_dropdown.get()
            ):
                self.selected_major = major.get()
                self.study_abroad = study_abroad.get()
                self.LOA = LOA.get()
                self.grad_early = grad_early.get()
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
            width=30,
        )
        major_dropdown.pack(pady=10)

        study_abroad = tk.StringVar()
        study_abroad.set("Do you plan to study abroad?")
        study_abroad_dropdown = ttk.Combobox(
            self.root,
            textvariable=study_abroad,
            values=[
                "N/A",
                "Sophomore  Fall",
                "Sophomore Spring",
                "Junior Fall",
                "Junior Spring",
                "Senior Fall",
                "Senior Spring",
            ],
            state="readonly",
            validate="all",
            width=30,
        )
        study_abroad_dropdown.pack(pady=10)

        LOA = tk.StringVar()
        LOA.set("Do you plan to take an LOA?")
        LOA_dropdown = ttk.Combobox(
            self.root,
            textvariable=LOA,
            values=[
                "N/A",
                "Sophomore  Fall",
                "Sophomore Spring",
                "Junior Fall",
                "Junior Spring",
                "Senior Fall",
                "Senior Spring",
            ],
            state="readonly",
            validate="all",
            width=30,
        )
        LOA_dropdown.pack(pady=10)

        grad_early = tk.StringVar()
        grad_early.set("Do you want to graduate early?")
        grad_early_dropdown = ttk.Combobox(
            self.root,
            textvariable=grad_early,
            values=["N/A", "One semester early", "One year early"],
            state="readonly",
            validate="all",
            width=30,
        )
        grad_early_dropdown.pack(pady=10)
        # Bind the selection event of the dropdown to the handle_major_selection function
        # major_dropdown.bind(
        #     "<<ComboboxSelected>>",
        #     handle_major_selection,
        # )
        grad_early_dropdown.bind(
            "<<ComboboxSelected>>",
            handle_major_selection,
        )

        # Initialize button
        button = ttk.Button(
            self.root,
            text="View 4 Year Course Plan",
            command=lambda: DataFrameViewer(
                self.root,
                CourseController.get_df(
                    self.selected_major, self.study_abroad, self.LOA, self.grad_early
                ),
            ),
        )
        button.pack_forget()  # Initially hide the button

        self.root.mainloop()
