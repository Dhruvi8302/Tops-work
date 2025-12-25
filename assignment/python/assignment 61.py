# Write a Python function to calculate the factorial of a number (a nonnegative integer) 
def factorial(n):
     if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
     result=1
     for i in range(1,n+1):
            result*=i
     return result
num=int(input("enter a number - "))
print(f"the factorial of {num} is {factorial(num)}")
    

    
