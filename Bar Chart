url = 'https://raw.githubusercontent.com/amosog-git/pandas/main/bece.csv'

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(url)

# Calculate the average score for each student
data["Average Score"] = data.iloc[:, 1:].mean(axis=1)

# Extract student names and average scores
student_names = data["Candidate Name"]
average_scores = data["Average Score"]

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.barh(student_names, average_scores, color="skyblue")
plt.xlabel("Average Score")
plt.ylabel("Candidate Name")
plt.title("Average BECE Scores by Student")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
