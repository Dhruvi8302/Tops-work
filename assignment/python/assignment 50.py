#check if a given key already exists in a dictionary. 
dict={'a':1,'b':5,'c':7}
user_input=input("enter a key ")
if user_input in dict.keys():
    print("key exists")
else:
    print("key does not exists")