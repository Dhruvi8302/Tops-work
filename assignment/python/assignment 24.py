#Python function to insert a string in the middle of a string
s=input("enter a string")
middle_str=len(s)//2
s2=input("enter a middle string")
main_str=(s[:middle_str] +s2 + s[middle_str:])
print(main_str)


