import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")
tips.head()

# Create a scatter plot of total bill vs. tip
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Total Bill vs. Tip")
plt.show()
