names = [" Ali ", " Sara ", " JOHN "]

clean_names = [name.strip().lower() for name in names] # Using a list comprehension to create a new list with cleaned names (stripped of whitespace and converted to lowercase)
print(clean_names)