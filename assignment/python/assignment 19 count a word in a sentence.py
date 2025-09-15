#count the occurrences of each word in a given sentence 
sentence=input("enter a sentence")
word=sentence.split()
# print(word)
count_word={}
for i in word:
    count_word[i]=word.count(i)
print(count_word)
