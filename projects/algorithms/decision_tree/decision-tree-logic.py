import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

# Generate synthetic dataset
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, 
                         n_classes=2, n_clusters_per_class=1, random_state=42)

# Train two decision tree classifiers with different depths
clf1 = DecisionTreeClassifier(max_depth=1, random_state=42)
clf1.fit(X, y)

clf2 = DecisionTreeClassifier(max_depth=5, random_state=42)
clf2.fit(X, y)

def plot_decision_boundary(clf, X, y, ax, title):
    # Define grid for decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    
    # Predict on grid points
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot decision boundary and points
    ax.contourf(xx, yy, Z, alpha=0.4, cmap='coolwarm')
    ax.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap='coolwarm')
    ax.set_title(title)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
plot_decision_boundary(clf1, X, y, axs[0], "Decision Tree (Depth = 1)")
plot_decision_boundary(clf2, X, y, axs[1], "Decision Tree (Depth = 5)")
plt.tight_layout()
plt.show()
