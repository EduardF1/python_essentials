# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       A)  list = [expression for item in iterable]
#                       B)  list = [expression for item in iterable if conditional]
#                       C)  list = [expression if/else for item in iterable]

# Example 1:
# squares = []                    # create an empty list
# for i in range(1, 11):          # create a for loop
#     squares.append(i * i)       # define what each loop iteration should do
# print(squares)

# squares = [i * i for i in range(1, 11)] # example usage of list comprehension
# print(squares)

# Example 2:
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 0]
# passed_students = list(filter(lambda x: x >= 60, students)) # A)
# passed_students = [i for i in students if i >= 60]    # B)

passed_students = [i if i >= 60 else "FAILED" for i in students]  # C)

print(passed_students)
