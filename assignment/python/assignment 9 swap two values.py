# Swapping using a temporary variable

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

# Swap using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping (with temp variable): a = {a}, b = {b}")

# Swapping without using a temporary variable

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

# Swap without a temp variable
a, b = b, a

print(f"After swapping (without temp variable): a = {a}, b = {b}")

