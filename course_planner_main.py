"""
Main program to set up and run the automated course planner
"""

import tkinter as tk

from vivian_view import CourseView

# from vivian_controller import CourseController


def main():
    root = tk.Tk()
    # controller = CourseController()

    view = CourseView(root)  # , controller)
    view.create_window()


if __name__ == "__main__":
    main()
