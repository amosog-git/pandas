# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(average_scores, labels=student_names, autopct="%1.1f%%", startangle=90)
plt.title("Average BECE Scores by Student")
plt.axis("equal")  # Equal aspect ratio ensures a circular pie chart

# Show the pie chart
plt.show()
