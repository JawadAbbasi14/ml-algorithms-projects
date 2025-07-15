import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv("dataset.csv")

# Features & labels
x = data[['Math', 'English', 'CS']]
y = data["Career_Path"]

# Encode target
label_encoder = LabelEncoder()
encoded_y = label_encoder.fit_transform(y)

# Train model with fewer neighbors
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, encoded_y)


# Prediction input
new_student = [[67, 67, 97]]
predicted = model.predict(new_student)
predicted_label = label_encoder.inverse_transform(predicted)[0]
print("Your career path is:", predicted_label)

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
