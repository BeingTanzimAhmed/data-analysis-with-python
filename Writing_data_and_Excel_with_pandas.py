import pandas as pd

# Create a sample DataFrame of Ecommerce orders
df = pd.DataFrame({
    'Order ID': [1, 2, 3],
    'Customer Name': ['Alice', 'Bob', 'Charlie'],
    'Product': ['Laptop', 'Smartphone', 'Headphones'],
    'Quantity': [1, 2, 1],
    'Price': [1200.00, 800.00, 150.00]
})

# Create a df for products
df2 = pd.DataFrame({
    'Product': ['Laptop', 'Smartphone', 'Headphones'],
    'Category': ['Electronics', 'Electronics', 'Accessories'],
    'product_id': [101, 102, 103],
    'product_description': ['High-performance laptop', 'Latest model smartphone', 'Noise-cancelling headphones'],
    'product_price': [1200.00, 800.00, 150.00]
})

# Write the DataFrame to an Excel file
with pd.ExcelWriter('ecommerce.xlsx') as writer: # Create an Excel writer object and specify the file name
    df.to_excel(writer, sheet_name='Orders', index=False)
    df2.to_excel(writer, sheet_name='Products', index=False)

print("DataFrames have been written to 'ecommerce.xlsx' successfully.")
print(df, df2)