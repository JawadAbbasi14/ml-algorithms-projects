import matplotlib.pyplot as plt
import numpy as np

def plot_decision_boundary(clf, X, y, ax, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.4)
    ax.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k')
    ax.set_title(title)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
plot_decision_boundary(clf1, X, y, axs[0], "Depth = 1")
plot_decision_boundary(clf2, X, y, axs[1], "Depth = 5")
plt.tight_layout()
plt.show()
