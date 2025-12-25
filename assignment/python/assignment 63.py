#function to check whether a number is perfect or not.
def is_perfect(n):
    if n <= 1:
        return False
    
    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
            
    return sum_of_divisors == n


num = int(input("Enter a number: "))
if is_perfect(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
