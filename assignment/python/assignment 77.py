#Write a Python program to read a file line by line store it into a variable
file=open('py.txt','r')
data=file.readlines()
A=data
print("A =", A)