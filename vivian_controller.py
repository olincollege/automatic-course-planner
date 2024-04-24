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

    def get_df(major, study_abroad):
        return CourseModel.get_required_courses(major, study_abroad)
