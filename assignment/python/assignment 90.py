# Write python program that user to enter only odd numbers, else will raise an exception.
class NotOddNumberError(Exception):
    pass

try:
    num = int(input("Enter an odd number: "))
    
    if num % 2 == 0:
        # Raise exception if number is even
        raise NotOddNumberError("Error: You entered an even number!")
    else:
        print("You entered a valid odd number:", num)
        
except ValueError:
    print("Error: That's not a valid integer!")
except NotOddNumberError as e:
    print(e)
