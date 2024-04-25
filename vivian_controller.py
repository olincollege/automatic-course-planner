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
    def __init__(self):
        pass

    def get_df(major, study_abroad, LOA, grad_early):
        """
        Gets the dataframe based on user input constraints

        Idk why this method is here, but i just need something
        in controller. Pressing the button could be here, but
        its jsut so much easier keeping everything in the tkinter
        class in view.
        """
        return CourseModel.get_required_courses(major, study_abroad, LOA, grad_early)
