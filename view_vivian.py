import pandas as pd

# Example DataFrame
columns = [
    "Semester 1",
    "Semester 2",
    "Semester 3",
    "Semester 4",
    "Semester 5",
    "Semester 6",
    "Semester 7",
    "Semester 8",
]
data = pd.DataFrame(None, index=range(4), columns=columns)

# Required Courses for E:C
electives = {"FoCS": "90%", "Discrete": "10%", "CompRobo": "50%"}

# Dictionary containing courses for each semester
sem_courses = {
    "Semester 1": ["QEA1", "Modsim", "DesNat", "AHS Concentration"],
    "Semester 2": ["QEA2", "ISIM", "Products & Markets", "Softdes"],
    "Semester 3": ["PIE", "Discrete"],
    "Semester 4": ["CD", "SoftSys"],
    "Semester 5": ["Bio", "MatSci"],
    "Semester 6": [electives],
    "Semester 7": ["Senior Capstone"],
    "Semester 8": ["Senior Capstone"],
}

# Loop through the dictionary and assign courses to DataFrame
for semester, courses in sem_courses.items():
    for i, course in enumerate(courses):
        data.at[i, semester] = course

# Fill the DataFrame with blank values for now
data = data.fillna("")

# Display the DataFrame
# data


# Create a function to check if a cell has a value and is a string
def is_string(val):
    return isinstance(val, str)


# Create a function to apply background color based on the condition
def highlight_strings(val):
    if is_string(val) and val != "":
        return "background-color: green"
    return ""


# Apply the style
styled_df = data.style.applymap(highlight_strings)

# Display the styled DataFrame
styled_df
