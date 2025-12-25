#function to check whether a number is in a given range
num=int(input("enter a number - "))
def is_in_range(num,start,end):
    return num in range(start,end+1)
if is_in_range(num,1,100):
    print(f"{num} is in the range 1 to 100")
else:
    print(f"{num} is not in the range 1 to 100")