
# logistic_plot.py

import matplotlib.pyplot as plt
from logistic import x, y, model
import numpy as np

# Generate values for smooth curve
x_range = np.linspace(min(x)[0], max(x)[0], 300).reshape(-1, 1)
y_prob = model.predict_proba(x_range)[:, 1]

# Plotting
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x_range, y_prob, color='red', label='Logistic Curve')
plt.axhline(0.5, color='gray', linestyle='--')
plt.xlabel("Marks")
plt.ylabel("Pass Probability")
plt.title("Logistic Regression Prediction")
plt.legend()
plt.grid(True)
plt.show()
