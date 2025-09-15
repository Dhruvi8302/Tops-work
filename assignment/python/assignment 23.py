#string made of the first 2 and the last 2 chars from a given a string
s = input("Enter a string: ")

if len(s) < 2:
    print("")
else:
    print(s[:2] + s[-2:])
