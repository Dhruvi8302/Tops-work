# script to sort (ascending and descending) a dictionary by value. 
data={'apple': 10, 'banana': 5, 'orange': 7, 'mango': 3}
ans=tuple(data.items())
print(ans)
ascending=dict(sorted(data.items(),key=lambda item: item[1]))
print(ascending)