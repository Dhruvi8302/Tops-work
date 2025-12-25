# Write a Python program to read last n lines of a file. 
file=open("test.txt", "r") 
lines = file.readlines()   

# print last lines
for line in lines[-1:]:
    print(line, end="")
