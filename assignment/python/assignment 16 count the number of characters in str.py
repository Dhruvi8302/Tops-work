# count the number of characters (character frequency) in a string 
str="helloooo"
char_freq={}
for i in str:
    char_freq[i]=str.count(i)
print(char_freq)