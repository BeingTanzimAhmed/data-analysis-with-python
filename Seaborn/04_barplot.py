import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a bar plot of day vs. total bill
sns.barplot(x="day", y="total_bill", data=tips, palette="Set3")
plt.title("Average Total Bill by Day")
plt.show()