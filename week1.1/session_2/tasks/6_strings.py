# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")                      # Prints the string on a new line
print(f"Modified String 1: {user_string.lower()}")              # Prints the string entirely in lowercase
print(f"Modified String 2: {user_string.upper()}")              # Prints the string entirely in uppercase
print(f"Modified String 3: {user_string.strip()}")              # Prints the string with no whitespace before or after the characters
print(f"Modified String 4: {user_string.replace('a', '@')}")    # Prints the string with all instance of 'a' replaced with '@'
print(f"Modified String 5: {user_string.capitalize()}")         # Prints the string with only the first character capitalised
print(f"Modified String 6: {user_string[::-1]}")                # Prints the string backwards
print(f"Modified String 7: {user_string.title()}")              # Prints the string with every word capitalised
print(f"Modified String 8: {len(user_string)}")                 # Prints the number of characters in the string
print(f"Modified String 9: {user_string.find('a')}")            # Prints the index of the first instance of 'a', or -1 if there is no instance
print(f"Modified String 10: {user_string.count('a')}")          # Prints the number of times 'a' is repeated in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # Prints true if the string starts with hello
print(f"Modified String 12: {user_string.endswith('!')}")       # Prints true if the string ends with an exclamation mark
print(f"Modified String 13: {user_string.isalnum()}")           # Prints true if the string is both non-empty and contains letters and digits
print(f"Modified String 14: {user_string.isalpha()}")           # Prints true if the string is both non-empty and contains only letters
print(f"Modified String 15: {user_string.isdigit()}")           # Prints true if the string is both non-empty and contains only digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!