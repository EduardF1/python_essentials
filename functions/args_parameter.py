# *args = parameter that will pack all (positional) arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
#         ! Can be named as whatever but the `*` symbol needs to be specified (i.e.: *params, *stuff etc.),
#         however, the common convention is to name it `args`

def add(*params):
    sum = 0
    params = list(params)
    params[0] = 0
    for i in params:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7))

# Note: tuples are  ordered and unchangeable, if modifications are required, the tuple collection can be
#       casted to a list (mutable).
