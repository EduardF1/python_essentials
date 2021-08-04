# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned values are used as arguments for the next outer function

# Expanded algorithm
# num = input('Enter a whole possitive number: ')
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# Composed algorithm
print(round(abs(float(input('Enter a whole positive number: ')))))