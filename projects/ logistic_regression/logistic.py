# logistic.py

import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample data
x = np.array([[10], [20], [50], [60], [90]])
y = np.array([0, 0, 1, 1, 1])

# Model training
model = LogisticRegression()
model.fit(x, y)

# Prediction example
sample = [[55]]
prediction = model.predict(sample)
print(f"Predicted class for {sample[0][0]}: {prediction[0]}")

