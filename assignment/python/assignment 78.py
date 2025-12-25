# Write a python program to find the longest words
file = open("test.txt", "r")
text = file.read()
file.close()

words = text.split()

longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word is:", longest)
