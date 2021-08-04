name = 'ronaldo'

# print the length of the str.
print(len(name))

# print the first index where the specified character is found
print(name.find('n'))

# print the string capitalized (the first letter will be uppercase)
print(name.capitalize())

# print the entire string in uppercase
print(name.upper())

# print the entire string in lowercase
print(name.lower())

# False in this case, if the string was '123' the output would be `True`
print(name.isdigit())

# True if the string consists only of alphabetic characters, False otherwise (also for ` `)
print(name.isalpha())

# Count how many occurrences of the specified character are in the string
print(name.count('o'))

# Arguments: character_to_replace, character_to_replace_with
print(name.replace('o','e'))

# Language feature, prints the specified string in a repetitive sequence
print(name*3)