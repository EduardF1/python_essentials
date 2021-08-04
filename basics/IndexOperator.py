# index operator `[]` = gives access to a sequence's element (str,list, tuples)

name = "Mark Henry VIII!"

# def decapitalize(str):
#     if not str:
#         return str
#     return str[0].lower() + str[1:]
#
#
# if name[0].isupper():
#     name = decapitalize(name)

first_name = name[:4].upper()
last_name = name[5:].lower()
last_character = name[-1]  # access the last index of the sequence
print(first_name)
print(last_name)
print(last_character)
