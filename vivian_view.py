import tkinter as tk
from tkinter import ttk
from pandastable import Table, TableModel
import pandas as pd
import random

from vivian_controller import CourseController
from vivian_model import CourseModel

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
        self.major = ""
        self.study_abroad = ""
        self.loa = ""
        self.grad_early = ""

        # self.controller = CourseController()
        self.controller = CourseController(
            self.major, self.study_abroad, self.loa, self.grad_early
        )

    def create_window(self):
        """
        Show and run the event of getting user input
        """

        def handle_major_selection(event):
            # if major_dropdown.get():
            #     self.selected_major = major.get()
            #     print("Selected:", self.selected_major)

            if (
                major_dropdown.get()
                and study_abroad_dropdown.get()
                and loa_dropdown.get()
                and grad_early_dropdown.get()
            ):
                self.major = major.get()
                self.loa = loa.get()
                self.study_abroad = study_abroad.get()
                self.grad_early = grad_early.get()

                self.controller = CourseController(
                    self.major, self.study_abroad, self.loa, self.grad_early
                )

                button.pack(padx=10, pady=10)
            else:
                # Hide button
                button.pack_forget()

        # Create Tkinter root window
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
            ],
            state="readonly",
            validate="all",
            width=30,
        )
        major_dropdown.pack(pady=10)

        loa = tk.StringVar()
        loa.set("Do you plan to take an LOA?")
        loa_dropdown = ttk.Combobox(
            self.root,
            textvariable=loa,
            values=[
                "N/A",
                # "Sophomore  Fall",
                # "Sophomore Spring",
                # "Junior Fall",
                # "Junior Spring",
                # "Senior Fall",
                # "Senior Spring",
                "sophomore fall",
                "sophmore spring",
                "junior fall",
                "junior spring",
                "senior fall",
                "senior spring",
            ],
            state="readonly",
            validate="all",
            width=30,
        )
        loa_dropdown.pack(pady=10)

        study_abroad = tk.StringVar()
        study_abroad.set("Do you plan to study abroad?")
        study_abroad_dropdown = ttk.Combobox(
            self.root,
            textvariable=study_abroad,
            values=[
                "N/A",
                # "Sophomore Fall",
                # "Sophomore Spring",
                # "Junior Fall",
                # "Junior Spring",
                # "Senior Fall",
                # "Senior Spring",
                "sophomore fall",
                "sophmore spring",
                "junior fall",
                "junior spring",
                "senior fall",
                "senior spring",
            ],
            state="readonly",
            validate="all",
            width=30,
        )
        study_abroad_dropdown.pack(pady=10)

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

        # Once the last dropdown has been selected, show the button
        grad_early_dropdown.bind(
            "<<ComboboxSelected>>",get_possible_semesters
            handle_major_selection,
        )

        # Initialize button
        button = ttk.Button(
            self.root,
            text="View 4 Year Course Plan",
            command=lambda: DataFrameViewer(
                self.root,
                self.controller.get_df(),
            ),
        )
        button.pack_forget()  # Initially hide the button

        self.root.mainloop()
