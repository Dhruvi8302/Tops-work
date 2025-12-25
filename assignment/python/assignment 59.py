#Write a Python program to create a dictionary from a string
#Note: Track the count of the letters from the string. 
str="Dhruviii"
dict={}

for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)