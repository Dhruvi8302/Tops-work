#reverse a string if its length is a multiple of 4
s = input("Enter a string: ")

if len(s) % 4 == 0:
    print("Reversed:", s[::-1])
else:
    print("Original:", s)
