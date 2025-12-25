# function that takes a list and returns a new list with unique elements of the first list
lst=[1,2,2,22,5,6,1,8,2,8,2,85]
unique_lst=[]
for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)
print(unique_lst)