#count the number of strings 
# where the string  length is 2 or more and 
# the first and last character are same from a given list of strings


words = ['abc','xxx','12251','12','aba','aa']
count = 0

# where the string  length is 2 or more and 
for word in words:
    length_of_word = len(word)
#    print(word)
    if length_of_word >= 2:
# the first and last character are same from a given list of strings
        first_character = word[0]
        last_character = word[-1]
        if first_character == last_character:
            count = count + 1
            print(f"'{word}' matches the condition.")
        else:
            print(f"'{word}' does not match (different first and last characters).")
    else:
        print(f"'{word}' is too short (length less than 2).")

print("\nTotal number of strings that match the condition:", count)




