import time

################
# While loops ##
################

# while loop = statement that will execute the contained block of code
#              as long as the test is true

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello " + name)

# alternative

# name = None
# while not name:
#     name = input("Enter your name: ")
#
# print("Hello " + name)

################
# For loops   ##
################

# for loop = a statement that will execute a block of code a limited amount of times
# while loop = unlimited / for loop = limited

# print the numbers [0,10]
# for i in range(10):
#    print(i+1)

# print the numbers [50,100]
# range(lower_bound, upper_bound) -> no_of_iterations: (upper_bound - lower_bound), the upper_bound is exclusive
# for i in range(50, 100 + 1):
#     print(i)

# print the numbers [50,100] with an iteration step of 2
# for i in range(50, 100 + 1, 2):
#     print(i)

# iterate through a string and print its letters
# for i in "Reddis":
#     print(i)

# countdown loop [0,10] and -1 (step)
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)   # make the thread sleep for 1s
# print("Happy New Year!")

###################
# Nested loops   ##
###################

# The "inner loop" will terminate all its iterations before finishing one iteration of the "outer loop"

# rows = int(input("How many rows?:"))
# columns = int(input("How many columns?:"))
# symbol = input("Enter a symbol to use:")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# Loop control statements = manipulate loop execution sequence
#   break = terminate the loop entirely
#   continue = skip to next iteration
#   pass = do nothing, acts as a placeholder

# while True:
#     name = input("Enter your name:")
#     if name != "":
#         break

# phone_number = "123-456-7890"
#
# # by adding `end=""` we prevent the print function's default (jump to a newline)
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)