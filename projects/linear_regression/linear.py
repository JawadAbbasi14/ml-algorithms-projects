# linear.py

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([[10], [20], [30], [40], [50]])
y = np.array([15, 25, 35, 45, 55])

# Model training
model = LinearRegression()
model.fit(x, y)

# Prediction
sample = [[35]]
prediction = model.predict(sample)
print(f"Predicted value for {sample[0][0]}: {prediction[0]}")

