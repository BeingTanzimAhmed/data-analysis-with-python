import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a heatmap of day vs. total bill
tips_pivot = tips.pivot_table(values="total_bill", index="day", columns="time", aggfunc="mean")
print(tips_pivot)
sns.heatmap(tips_pivot, annot=True, cmap="coolwarm")
plt.title("Heatmap of Total Bills by Day and Time")
plt.show()