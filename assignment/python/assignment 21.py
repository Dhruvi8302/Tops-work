#word change with ing,ly
word = input("Enter a word: ")

if len(word) < 3:
    result = word
elif word.endswith("ing"):
    result = word + "ly"
else:
    result = word + "ing"

print("Result:", result)
