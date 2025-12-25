#find the highest 3 values in a dictionary
dict = {'a': 5, 'b': 9, 'c': 2, 'd': 15, 'e': 7}

top3_values = sorted(dict.values(), reverse=True)[:3]
print("The highest 3 values are:", top3_values)
