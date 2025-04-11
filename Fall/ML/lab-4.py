import numpy as np
import matplotlib.pyplot as plt
from lab_utils_multi import load_house_data, run_gradient_descent
import lab_utils_common
# Load the data
x_train, y_train = load_house_data()
X_features = ['size(sqft)', 'bedrooms', 'floors', 'age']

# Create a figure with 4 subplots, sharing the y-axis
fig, ax = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

# Plot each feature against the target variable
for i in range(len(ax)):
    ax[i].scatter(x_train[:, i], y_train)
    ax[i].set_xlabel(X_features[i])  # Use ax[i] to set the xlabel for each subplot

ax[0].set_ylabel("Price (1000's)")
plt.show()

_, _, hist = run_gradient_descent(x_train, X_features, 10 , alpha=9.9e-7)