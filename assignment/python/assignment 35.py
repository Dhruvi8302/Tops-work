
#generate and print a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30

# Generate list of squares of numbers from 1 to 30
squares = [x*x for x in range(1, 31)]

# Print the list
print("All squares:", squares)

# Print the first 5 and last 5 elements
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])
