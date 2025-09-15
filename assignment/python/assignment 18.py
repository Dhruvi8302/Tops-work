main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

occurrences = main_string.count(substring)

print(f"The substring '{substring}' occurs {occurrences} times in the string.")
