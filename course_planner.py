"""
Main program to set up and run the automated course planner
"""

import tkinter as tk

from vivian_view import CourseView


def main():

    root = tk.Tk()

    view = CourseView(root)
    view.create_window()


if __name__ == "__main__":
    main()
