"""
Get user input from dropdowns (major for now)
"""

import tkinter as tk
from tkinter import ttk
from pandastable import Table, TableModel
import pandas as pd
import random

from vivian_model import CourseModel


class CourseController:
    """
    This controller helps points to correct functions to run in model
    """

    def __init__(self, major, study_abroad, loa, grad_early):
        self.model = CourseModel(major, study_abroad, loa, grad_early)

    # Methods should be in order of which ones to run first
    def major_constraint(self):
        """
        Point to correct model function(s) to fill major required courses
        """
        self.model.fill_major_required_courses()

    def study_abroad_constraint(self):
        """
        Point to correct model function(s) to fill study abroad semester
        """
        self.model.fill_study_abroad()

    def loa_constraint(self):
        """
        Point to correct model function(s) to fill loa semester
        """
        self.model.fill_loa()

    def grad_early_constraint(self):
        """
        Point to correct model function(s) to fill graduating early semesters
        """
        self.model.fill_grad_early()

    def fill_other_requirements(self):
        """
        Point to correct model function(s) to fill other requirements (major electives, AHS,)
        """
        self.model.fill_other_requirements()

    def fill_empty_schedule(self):
        """
        Point to correct model function(s) to fill rest of empty schedule
        """

        self.model.fill_empty_schedules()

    def get_df(self):
        """
        Fills out and returns a full dataframe of courses
        """
        # Constrain the model with user constraints
        # self.loa_constraint()  # will set max num of courses
        # self.major_constraint()
        # self.study_abroad_constraint()
        # self.grad_early_constraint()

        # # self.fill_other_requirements()
        # self.fill_empty_schedule()

        # self.fill_empty_schedule()

        # Other contraints -- other requirements, major electives

        return self.model.get_df()
