# Write a Python program to write a list to a file

my_list = ["apple", "banana", "cherry", "date","grapes"]

# Open file in write mode
file=open("sample.txt", "w") 
for item in my_list:
    file.write(item + "\n")  # write each item on a new line

print("List has been written to the file.")
