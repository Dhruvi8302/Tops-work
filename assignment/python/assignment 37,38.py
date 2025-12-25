#assignment 37
# convert a list of characters into a string
lst=['d','v','g','h']
str=''.join(lst)
print(str)


#assignment 38
# select an item randomly from a list
import random
lst=[4,5,6,7,9,5,85,94,78,29]
random_item=random.choice(lst)
print(random_item)


lst=[4,5,6,7,9,5,85,94,78,29]
for i in lst:
    a=random.randint(0,len(lst)-1)
print(a)




