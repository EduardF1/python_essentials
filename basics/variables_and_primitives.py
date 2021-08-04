#################
# 1) Strings    #
#################

# variable = container for a value, behaves as the value that it contains.
# Best practice for variable naming is to separate composite names with an `_`.
first_name = 'ED'
last_name = 'FIS'
full_name = first_name + last_name

print('Hello' + ' ' + full_name)
# to check the type of a variable, we can use the `type` function

print(type(first_name))
# Output: <class 'str'> which is shorthand for string

#################
# 2) Integers   #
#################
age = 23
age += 1
print(age)
# Output: <class 'int'> which is shorthand for integer
print(type(age))
# In Py., simple concatenation is not possible, will result in a type
# mismatch, thus we need to use type casting `str(age)` -> casts the int
# to a str.
print('Your age is: ' + str(age))

#################
# 3) Floats     #
#################

height = 250.5
print('Your height is: ' + str(height) + 'cm')
print(type(height))

#################
# 4) Bool(eans) #
#################

human = False
print("Are you a " + str(not human))
# Output: <class 'bool'> which is shorthand for string
print(type(human))