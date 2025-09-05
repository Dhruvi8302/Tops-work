n = int(input("Enter a positive integer (n): "))
if n > 0:
    total = n * (n + 1) // 2
    print(f"The sum of the first {n} positive integers is: {total}")
else:
    print("Please enter a positive integer greater than 0.")

#calculate the length of a string
user_string = input("Enter a string: ")
print(len(user_string))
