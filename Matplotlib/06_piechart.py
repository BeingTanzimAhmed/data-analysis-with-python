import matplotlib.pyplot as plt
import numpy as np

sizes = [40, 35, 25]
labels = ["A", "B", "C"]

plt.style.use("ggplot")

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()