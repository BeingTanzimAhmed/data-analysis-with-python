numbers = [1, 2, 3, 4, 5]

# Using a for loop to create a new list with squares
squares = []

for num in numbers:
    squares.append(num ** 2)
print(squares)

# Using a list comprehension to create a new list with squares
squares_comp = [num ** 2 for num in numbers]
print(squares_comp)