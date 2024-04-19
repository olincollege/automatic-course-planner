import pandas as pd

# Create column names for each semester
columns = [
    "Freshmen Fall",
    "Freshmen Spring",
    "Sophomore Fall",
    "Sophomore Spring",
    "Junior Fall",
    "Junior Spring",
    "Senior Fall",
    "Senior Spring",
]
# Create an empty DataFrame with 4 rows and 8 columns
data = pd.DataFrame(index=range(0, 4), columns=columns)

# Fill the DataFrame with blank values for now
data = data.fillna("")

# Required Courses for E:C
# electives = ["FoCS", "Discrete", "CompRobo"]

# Sem 1
sem1_courses = ["QEA1", "Modsim", "DesNat", "AHS Concentration"]
for i, item in enumerate(sem1_courses):
    data.loc[i, columns[0]] = item

# Sem 2
sem2_courses = ["QEA2", "ISIM", "Products & Markets", "Softdes"]
for i, item in enumerate(sem2_courses):
    data.loc[i, columns[1]] = item

# Sem 3
sem3_courses = ["PIE", "Discrete"]
for i, item in enumerate(sem3_courses):
    data.loc[i, columns[2]] = item

# Sem 4
sem4_courses = ["CD", "SoftSys"]
for i, item in enumerate(sem4_courses):
    data.loc[i, columns[3]] = item

# Sem 5
sem5_courses = ["Bio", "MatSci"]
for i, item in enumerate(sem5_courses):
    data.loc[i, columns[4]] = item

# Sem 7
sem7_courses = ["Senior Capstone"]
for i, item in enumerate(sem7_courses):
    data.loc[i, columns[6]] = item

# Sem 8
sem8_courses = ["Senior Capstone"]
for i, item in enumerate(sem8_courses):
    data.loc[i, columns[7]] = item


return data
