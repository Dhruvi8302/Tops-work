# How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 
     
        #In Python, exceptions are handled using try, except, and finally blocks to 
        # prevent program crashes and handle errors gracefully.

try:
    no=int(input("enter a number "))
    no1=int(no)
    print(f"value is {no1}")

    ans=no1/2
    print(f'ans {ans}')
except ZeroDivisionError:
    print("there is an ZeroDivisionError")
except ValueError:
    print("there ia an value error")

finally:
    print("have a great day!!!")