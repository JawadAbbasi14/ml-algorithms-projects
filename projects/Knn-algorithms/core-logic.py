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
