# str.format() =    optional method that gives users more control when displaying output

animal = 'cow'
item = 'moon'

# `{}` are placeholders (format fields) which are replaced in-order by values or variables
# Method 1 :using the default language feature (does not allow reusability of arguments)
# print('The {} jumped over the {}'.format(animal, item))

# Method 2: using positional arguments (explicitly specify the index of the arguments)
#           allows reusability of arguments through the index specification
# print('The {0} jumper over the {1}'.format(animal, item))
# print('The {0} jumper over the {0}'.format(animal, item))

# Method 3: using keyword arguments
#           allows reusability of arguments through key specification
# print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))
# print('The {animal} jumped over the {animal}'.format(animal='cow', item='moon'))

# A more elegant approach
# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# Adding padding
name = 'Peter'
print("Hallo ,Ich heisse {}".format(name))
print("Hallo ,Ich heisse {:10}. Schön, dich kennenzulernen".format(name))
print("Hallo ,Ich heisse {:<10}. Schön, dich kennenzulernen".format(name))  # precede string with (str.len - 10) empty spaces to the right
print("Hallo ,Ich heisse {:>10}. Schön, dich kennenzulernen".format(name))  # precede string with (str.len - 10) empty spaces to the left
print("Hallo ,Ich heisse {:^10}. Schön, dich kennenzulernen".format(name))  # center string within the 10 empty spaces (L:2 - str - R:3)

# Format numbers
number = 3.14159

print("The number PI is {:.2f}".format(number))  # output 3.14
print("The number PI is {:.3f}".format(number))  # output 3.142 (rounds the number by default)

number = 1000

print("The number is {:,}".format(number))  # output 1,000
print("The number is {:b}".format(number))  # output binary rep. of the given number
print("The number is {:o}".format(number))  # output octal rep. of the given number
print("The number is {:X}".format(number))  # output hex (uppercase) rep. of the given number
print("The number is {:x}".format(number))  # output hex (lowercase) rep. of the given number
print("The number is {:E}".format(number))  # output scientific notation (uppercase) of the number
print("The number is {:e}".format(number))  # output scientific notation (lowercase) of the number
