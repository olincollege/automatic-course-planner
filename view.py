"""
Viewer class shows the Tkinter window and handles selection
"""

import tkinter as tk
from tkinter import ttk
from pandastable import Table

from controller import CourseController


class DataFrameViewer(tk.Toplevel):
    """
    A class for displaying a pandas DataFrame in a Tkinter window.

    Attributes:
        parent: The parent Tkinter window.
        dataframe: The pandas DataFrame to be displayed.

    Methods:
        __init__: Initializes the DataFrameViewer.
    """

    def __init__(self, parent, dataframe):
        """
        Initializes the DataFrameViewer.

        Args:
            parent: The parent Tkinter window.
            dataframe: The pandas DataFrame to be displayed.

        Returns:
            None
        """

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

        # pylint: disable=too-few-public-methods


class CourseView:
    """
    A class for displaying and interacting with the course selection interface.

    Attributes:
        root: The Tkinter root window.
        major: The selected major.
        study_abroad: The selection for studying abroad.
        loa: The selection for taking an LOA.
        grad_early: The selection for graduating early.
        controller: An instance of CourseController for managing course data.

    Methods:
        __init__: Initializes the CourseView.
        create_window: Creates and displays the course selection interface.
    """

    def __init__(self, root):
        """
        Initializes the CourseView.

        Args:
            root: The Tkinter root window.

        Returns:
            None
        """
        self.root = root
        self.major = ""
        self.study_abroad = ""
        self.loa = ""
        self.grad_early = ""
        self.controller = CourseController(
            self.major, self.study_abroad, self.loa, self.grad_early
        )

    def create_window(self):
        """
        Creates and displays the course selection window.

        Returns:
            None
        """

        def handle_major_selection(event):
            # pylint: disable=unused-argument
            """
            Event handler for major selection.

            Args:
                event: The event object.

            Returns:
                None
            """
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
            "<<ComboboxSelected>>",
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

        self.root.mainloop()
