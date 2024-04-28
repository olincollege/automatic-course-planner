"""
Get user input from dropdowns (major for now)
"""

import tkinter as tk
from tkinter import ttk
from pandastable import Table, TableModel
import pandas as pd
import random

from test_model import CourseModel


class CourseController:
    def __init__(self, major, study_abroad, LOA, grad_early):
        self.model = CourseModel(major, study_abroad, LOA, grad_early)

    # make an object of the course model class - with all user inputs
    # call the get_df functon by obj.get_df

    def get_df(self):
        """
        Gets the dataframe based on user input constraints

        Idk why this method is here, but i just need something
        in controller. Pressing the button could be here, but
        its jsut so much easier keeping everything in the tkinter
        class in view.
        """
        return self.model.get_df()

    # def handle_major_selection(event):
    #     if (
    #         major_dropdown.get()
    #         and study_abroad_dropdown.get()
    #         and LOA_dropdown.get()
    #         and grad_early_dropdown.get()
    #     ):
    #         # self.selected_major = major.get()
    #         # self.study_abroad = study_abroad.get()
    #         # self.LOA = LOA.get()
    #         # self.grad_early = grad_early.get()

    #         # Show button
    #         button.pack(padx=10, pady=10)
    #     else:
    #         # Hide button
    #         button.pack_forget()
