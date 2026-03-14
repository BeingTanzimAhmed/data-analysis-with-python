import pandas as pd

# Create a DataFrame from a dictionary

data = {
    "name": ["Ali", "Sara", "John"],
    "marks": [85, 90, 78]
}

df = pd.DataFrame(data) # df is a variable that holds the DataFrame created from the data dictionary
# print(df) # This will print the DataFrame to the console

# print(df.head()) # This will print the first 5 rows of the DataFrame. Since our DataFrame has only 3 rows, it will print all of them.
# print(df.tail()) # This will print the last 5 rows of the DataFrame. Again, since our DataFrame has only 3 rows, it will print all of them.
# print(df.info()) # This will print a summary of the DataFrame, including the number of non-null entries, data types of each column, and memory usage.
# print(df.describe()) # This will print a statistical summary of the numerical columns in the DataFrame, including count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum values.

# print(df["marks"]) # This will print the "marks" column of the DataFrame. It will return a Series object containing the marks for each student.
# print(df[["name", "marks"]]) # This will print both the "name" and "marks" columns of the DataFrame. It will return a new DataFrame containing only these two columns.