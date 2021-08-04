# **kwargs =    parameter that will pack all (keyword) arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments
#               ! Can be name differently (but `**` need to precede the name), i.e.: `dict_params`
#               but the common convention is to use `kwargs` which stands for `keyword arguments`.

def hello(**names):
    space_character = ' '
    # print('Hello ' + kwargs['first'] + space_character + kwargs['middle'] + space_character + space_character + kwargs['last'])
    print('Hello', end=space_character)
    for key, value in names.items():
        print(value, end=space_character)


hello(title='Mr.', first='Jack', middle='Nicholson', last='DeSanta')
