# to unzip a list of tuples into individual lists

data=[(4,5),(7,8),(9,10)]
list1,list2=zip(*data)
print("list 1 :" ,list(list1))
print("list 2 :", list(list2))


