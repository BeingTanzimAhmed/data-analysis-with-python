import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a count plot of day vs. total bill
sns.countplot(x="day", data=tips, palette="Set2")
plt.title("Count of Total Bills by Day")
plt.show()