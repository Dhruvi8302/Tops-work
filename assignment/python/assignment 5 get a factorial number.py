#get a factorial number

number=int(input("enter a number"))
factorial=1

# Check if the number is negative
if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1,number+1):
        factorial*=i
    print(f"the factorial of {number} is {factorial}")