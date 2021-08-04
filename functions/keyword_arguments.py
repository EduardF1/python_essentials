# keyword arguments = arguments preceded by an identifier when they are passed to a function
#                      The order of the arguments doesn't matter, unlike positional arguments
#                      Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print('Hello ' + first + ' ' + middle + ' ' + last)


# Example  call to hello() using positional arguments (the argument order matters)
# hello('John', 'Garcia', 'NuxtJS')

# Example of call to hello() using keyword arguments
hello(last='NuxtJS', middle='Garcia', first='John')
