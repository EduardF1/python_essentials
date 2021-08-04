# scope = the region in which a variable is recognized
#         A variable is only available from inside the region where it is created
#         A global and locally scoped versions of a variable can be created

name = "There might be another way..."  # a global scope variable (available inside & outside functions but only in the module/class where it is declared)


def display_name():
    name = 'Code like there is no tomorrow...'  # a local scope variable (available only within the function where the var. is declared)
    print(name)


display_name()
print(name)

# Python uses the L.E.G.B principle to access variables
#          Priority of selection
# L - Local         │
# E - Enclosing     │
# G - Global        │
# B - Built-in      ↓
