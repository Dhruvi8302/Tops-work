#checks whether a passed string is palindrome or not 
def is_palindrome(s):
    s="".join(ch for ch in s.lower() if ch.isalnum())
    return  s==s[::-1]


text = input("Enter a string: ")
if is_palindrome(text):
    print(f"{text} is a Palindrome")
else:
    print(f"{text} not a palindrome")
