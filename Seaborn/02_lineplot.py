import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a line plot of total bill vs. tip
sns.lineplot(x="total_bill", y="tip", data=tips, marker="o", color="green", linestyle="--")
plt.style.use("ggplot")
plt.title("Total Bill vs. Tip")
plt.show()