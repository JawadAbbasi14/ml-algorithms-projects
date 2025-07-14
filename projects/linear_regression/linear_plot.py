
# linear_plot.py

import matplotlib.pyplot as plt
from linear import x, y, model
import numpy as np

# Generate line for predictions
x_line = np.linspace(min(x)[0], max(x)[0], 100).reshape(-1, 1)
y_line = model.predict(x_line)

# Plotting
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x_line, y_line, color='green', label='Prediction Line')
plt.xlabel("Marks")
plt.ylabel("Output")
plt.title("Linear Regression Fit")
plt.legend()
plt.grid(True)
plt.show()
