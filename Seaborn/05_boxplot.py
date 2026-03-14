import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a box plot of day vs. total bill
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Distribution of Total Bills by Day")
plt.show()