from tkinter import *


# What major?
major = ["MechE", "ECE", "E:C", "E:Robo", "E:Sus", "E:Design", "E:Bio"]
# LOA? Which Semester?
loa = False
loa_semester = [1, 2, 3, 4, 5, 6, 7, 8, "I will not take an LOA."]
# Study Abroad? Which Semester?
study_abroad = False
study_abroad_semester = [1, 2, 3, 4, 5, 6, 7, 8, "I will not study away."]
# Graduate Early?
graduate_early = False
graduate_early_semester = [1, 2, "I will not graduate early."]
# Which Capstone?
capstone = ["SCOPE", "ADE", "TVC"]

# instance of Tkinter frame
root = Tk()
# set size of window
root.geometry("1000x800")

# Create a canvas object
# not resolved: canvas looks weird when it runs (there's a split in the middle and doesn't size right)
canvas = Canvas(root, height=800, width=1000, bg="PowderBlue")


# label to display text about major
lf = LabelFrame(canvas)

label = Label(lf, text="What is your major?")
label.config(font="Arial 12")
label.pack(padx=10, pady=10)
lf.pack()


# first Tkinter drop down menu - major
def show():
    label.config(text=selected_major.get())


selected_major = StringVar()
selected_major.set("Not Selected")

drop = OptionMenu(canvas, selected_major, *major)
drop.pack()

label = Label(canvas, text=" ")
label.pack()


# label to display text about LOA
lf_loa = LabelFrame(canvas)

label_loa = Label(lf_loa, text="Will you take an LOA? Which semester?")
label_loa.config(font="Arial 12")
label_loa.pack(padx=10, pady=10)
lf_loa.pack()


# second drop down menu - LOA
def show_loa():
    label.config(text=selected_loa.get())


selected_loa = StringVar()
selected_loa.set("Not Selected")

drop_loa = OptionMenu(canvas, selected_loa, *loa_semester)
drop_loa.pack()

label_loa_two = Label(canvas, text=" ")
label_loa_two.pack()


# label to display text about study abroad
lf_sa = LabelFrame(canvas)

label_sa = Label(lf_sa, text="Will you study abroad? Which semester?")
label_sa.config(font="Arial 12")
label_sa.pack(padx=10, pady=10)
lf_sa.pack()


# third drop down menu - study abroad
def show_sa():
    label.config(text=selected_sa.get())


selected_sa = StringVar()
selected_sa.set("Not Selected")

drop_sa = OptionMenu(canvas, selected_sa, *study_abroad_semester)
drop_sa.pack()

label_sa_two = Label(canvas, text=" ")
label_sa_two.pack()


# label to display text about graduating early
lf_grad = LabelFrame(canvas)

label_grad = Label(lf_grad, text="Will you graduate early? By how many semesters?")
label_grad.config(font="Arial 12")
label_grad.pack(padx=10, pady=10)
lf_grad.pack()


# fourth drop down menu - graduate early
def show_grad():
    label.config(text=selected_grad.get())


selected_grad = StringVar()
selected_grad.set("Not Selected")

drop_grad = OptionMenu(canvas, selected_grad, *graduate_early_semester)
drop_grad.pack()

label_grad_two = Label(canvas, text=" ")
label_grad_two.pack()


# label to display text about senior capstone
lf_capstone = LabelFrame(canvas)

label_capstone = Label(lf_capstone, text="What will your senior capstone be?")
label_capstone.config(font="Arial 12")
label_capstone.pack(padx=10, pady=10)
lf_capstone.pack()


# fifth drop down menu - senior capstone
def show_capstone():
    label.config(text=selected_capstone.get())


selected_capstone = StringVar()
selected_capstone.set("Not Selected")

drop_capstone = OptionMenu(canvas, selected_capstone, *capstone)
drop_capstone.pack()

label_capstone_two = Label(canvas, text=" ")
label_capstone_two.pack()


# dummy buttons to make sure the user-inputted values are stored
def dummy_major():
    print("This is the value from the major option menu: ", selected_major.get())


dummy_button_major = Button(canvas, text="Dummy Major", command=dummy_major)
dummy_button_major.pack()


def dummy_loa():
    print("This is the value from the LOA option menu: ", selected_loa.get())


dummy_button_loa = Button(canvas, text="Dummy LOA", command=dummy_loa)
dummy_button_loa.pack()


def dummy_sa():
    print("This is the value from the study abroad option menu: ", selected_sa.get())


dummy_button_sa = Button(canvas, text="Dummy Study Abroad", command=dummy_sa)
dummy_button_sa.pack()


def dummy_grad():
    print(
        "This is the value from the graduate early option menu: ", selected_grad.get()
    )


dummy_button_grad = Button(canvas, text="Dummy Graduate Early", command=dummy_grad)
dummy_button_grad.pack()


def dummy_capstone():
    print(
        "This is the value from the senior capstone option menu: ",
        selected_capstone.get(),
    )


dummy_button_capstone = Button(
    canvas, text="Dummy Senior Capstone", command=dummy_capstone
)
dummy_button_capstone.pack()


canvas.pack()
root.mainloop()
