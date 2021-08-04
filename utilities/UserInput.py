# User input accepted by using the `input()` function
# input() returns a string, for mathematical operations, we
# will need to cast the output to int <> float
name = input('What is your name?: ')
age = int(input('How old are you?: '))
height = float(input('How tall are you?: '))

print('Hello' + ' ' + name)
print('You are ' + str(age) + ' years old')
print('You are ' + str(height) + ' cm tall')