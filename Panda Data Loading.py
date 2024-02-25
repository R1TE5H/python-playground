# Data Loading With Panda
import numpy as np
# Use the Panada Package
import pandas as pd

# txt Files
# The File does not Contain a Header
    # Using header = None prevents the first row of Data as being interpreted as a header
df1 = pd.read_csv('payroll-1.txt', sep = " ", header = None)

# Load a txt file while Specifying Column Names
    # Use a List with Column Names as Elements 
        # MUST be a list named "names"
df2 = pd.read_csv('payroll-1.txt', sep=" ", names = ["Employee", "Salary", "Year", "Gender"])

# Same file as Payroll-1 but a header is included within the txt file
    # Notice the output of df2 and df3 are the same
df3 = pd.read_csv('payroll-2.txt', sep=" ")

# Get Data from a File and Use it to Create a new Data Frame
x = []
y = []
z = []
w = []
ins = open("payroll-1.txt")
for line in ins:
    items = line.split()
    x.append(items[0])
    y.append(items[1])
    z.append(items[2])
    w.append(items[3])
df4  = pd.DataFrame({"Employee": x, "Salary": y, "Year": z, "Sex": w})

#----------------------------------------------------------------------------------------------

# Excel Files
    #pd.read_excel(Path to File, Sheet Number)
df5 = pd.read_excel("information.xlsx", "Sheet1")

#-----------------------------------------------------------------------------------------------

# CSV Files
# CSV File Does not Contain a Header
df6 = pd.read_csv("document.csv", header=None)

# Add a Label to the Index Column
df7 = pd.read_csv("document.csv", index_col="UID", names=["UID", "First Name", "Last Name"])

# Adding Headers and Changing the Order of the Columns
df8 = pd.read_csv('document.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name'])

# Create and Update a CSV File
    # Create a Data Frame with some type of Data
df9 = pd.DataFrame(np.random.randint(20,150,(3,3)), columns = ["A", "B", "C"])
    # Use the to_csv Function to convert it to a CSV File --> Pick the name of the File
df9.to_csv("mydata.csv")

# Search Through a Data Frame for a Specific Condition
    # Will Return All Rows/Columns that meet the Condition
z = df9.query("A>B or B<C")