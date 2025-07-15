
# Plot: Math vs CS
plt.figure(figsize=(8,6))
colors = ['red', 'green', 'blue', 'orange', 'purple']
unique_labels = sorted(data["Career_Path"].unique())

for i, label in enumerate(unique_labels):
    # Filter rows for this label
    group = data[data['Career_Path'] == label]
    plt.scatter(group['Math'], group['CS'], color=colors[i % len(colors)], label=label)

# Plot the new student
plt.scatter(new_student[0][0], new_student[0][2], color='black', label='Predicted: ' + predicted_label, marker='X', s=100)

plt.xlabel('Math Marks')
plt.ylabel('CS Marks')
plt.title('KNN Career Prediction (Math vs CS)')
plt.legend()
plt.grid(True)
plt.show()
