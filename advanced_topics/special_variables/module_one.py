# *************************************************************************
# if __name__ == '__main__'
# *************************************************************************
# Why ?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules
# The Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

# some programs will have a main() in which the main execution of the program will be placed
def main():
    print("Hello")


if __name__ == '__main__':
    main()
else:
    print("running other module indirectly")

# import module_two
#
# print(__name__)
# print(module_two.__name__)
