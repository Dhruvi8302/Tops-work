# check whether a list contains a sub list
lst=[1,5,7,9,1,7,[4,5,6]]

for i in lst:
    if type(i)==list:
        print("list contains sub list")
        break
else:
    print("list not contains sub list")