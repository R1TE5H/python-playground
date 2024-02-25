# Analyzing Grouped Data

# Use Panada and the Math Plot Library

import pandas as pd
import matplotlib.pyplot as plt

# Create a Data Frame using Panda
data = pd.DataFrame({"Gender": ["f", "f", "m", "f", "m", "m", "f", "m", "f", "m", "m"], 
                     "Hours/Day": [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,5.1, 3.9, 3.7, 2.1, 4.3],
                     "Race":["W", "W", "B", "H", "W", "A", "B", "H", "W", "A", "W"],
                     "Age":[20, 25, 17, 14, 14, 16,13, 21, 26, 28, 17]})

# Group Columns Together and Separate Based on First Row
grouped = data.groupby("Gender")

# Print Data Statistics
print(grouped.describe())

# Display a Box Plot
grouped.boxplot()
plt.show()