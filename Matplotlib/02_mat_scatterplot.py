import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.style.use("ggplot")

plt.scatter(x, y, s=100, c="green", alpha=0.7)
plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()