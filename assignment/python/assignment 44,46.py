#assignment 44


# Create a tuple with different data types
tuple= (25, "Hello", 3.14, True, [1, 2, 3], {'name': 'dhruvi'}, (10, 20))
print("Data types of each element:")
for i  in tuple:
    print(f"{i} -- {type(i)}")


#assignment 46
#convert a list of tuples into a dictionary
lst=[(1,'dhruvi'),(2,'hetvi'),(3,'dixita')]
ans=dict(lst)
print(ans)