items = ["apple", "banana", "cherry"]
prices = [0.5, 0.3, 0.2]

price_dict = {items[i]: prices[i] for i in range(len(items))} # Using a dictionary comprehension to create a new dictionary that maps items to their prices
print(price_dict)


scores = {"math": 80, "science": 90, "english": 75}

passed = {k: v for k, v in scores.items() if v >= 80} # Using a dictionary comprehension to create a new dictionary that includes only subjects with scores greater than or equal to 80
print(passed)