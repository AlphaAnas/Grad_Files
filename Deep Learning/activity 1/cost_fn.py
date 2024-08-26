import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

x = [12, 15, 18, 21, 24, 27]
y = [2.14, 2.32, 3.01, 3.57, 4.04, 4.48]

# Train the model
model = LinearRegression()
model.fit(np.array(x).reshape(-1, 1), y)

# Get the slope (m) and intercept (c)
m = model.coef_[0]
c = model.intercept_

# Print the equation of the line
print(f"The equation of the line is: y = {m:.2f}x + {c:.2f}")

# Plotting
plt.scatter(x, y, marker='x', c='r')
plt.plot(x, model.predict(np.array(x).reshape(-1, 1)), c='b')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(f"Mean Squared error: {mean_squared_error(y, model.predict(np.array(x).reshape(-1, 1))):.2f}")