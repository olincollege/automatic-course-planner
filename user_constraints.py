from tkinter import *


# What major?
major = ["MechE", "ECE", "E:C", "E:Robo", "E:Sus", "E:Design", "E:Bio"]
# LOA? Which Semester?
loa = False
loa_semester = [1, 2, 3, 4, 5, 6, 7, 8]
# Study Abroad? Which Semester?
study_abroad = False
study_abroad_semester = [1, 2, 3, 4, 5, 6, 7, 8]
# Graduate Early?
graduate_early = False
graduate_early_semester = [1, 2]
# Which Capstone?
capstone = ["SCOPE", "ADE", "TVC"]

# Tkinter drop down menu
root = Tk()

root.geometry("200x200")


def show():
    label.config(text=clicked.get())


clicked = StringVar()
clicked.set("Not Selected")

drop = OptionMenu(root, clicked, *major)
drop.pack()

# button = Button(root, text="click Me", command=show).pack()

label = Label(root, text=" ")
label.pack()

root.mainloop()
