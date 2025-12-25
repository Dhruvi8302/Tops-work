#Write a Python program to count the frequency of words in a file
file = open("test.txt", "r")
text = file.read()
file.close()

words = text.split()

freq = {}   # empty dictionary

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("Word frequency:")
for word, count in freq.items():
    print(word, ":", count)
