# sort() method = used with lists
# sort() function = used with iterables

# students = ["Klaus", "Jürgen", "Fritz-Patrick", "Hermmann", "Patrick", "Sebastian"]
# students = ("Klaus", "Jürgen", "Fritz-Patrick", "Hermmann", "Patrick", "Sebastian")

# sort array items alphabetically
# students.sort()
# for i in students:
#     print(i)

# sort array items (reversed) alphabetically
# students.sort(reverse=True)
# for i in students:
#     print(i)

# sort students tuple
# sorted_students = sorted(students)
# for i in sorted_students:
#     print(i)

# sort students tuple (reversed order)
# sorted_students = sorted(students, reverse=True)
# for i in sorted_students:
#     print(i)

# list of tuples
# Format: soldier_name, division, age
# students = [("Klaus", "F", 22),
#             ("Jürgen", "B", 30),
#             ("Fritz-Patrick", "C", 40),
#             ("Hermmann", "X", 50),
#             ("Patrick", "Y", 22),
#             ("Sebastian", "A", 34)]
#
# student_age = lambda age: age[2]
# student_division = lambda division: division[1]
#   the keyword argument `key` takes a function as an argument
#   to sort the list in reverse order, we can add `reverse=True`
# students.sort(key=student_division)
# for i in students:
#     print(i)

# tuple of tuples
students = (("Klaus", "F", 22),
            ("Jürgen", "B", 30),
            ("Fritz-Patrick", "C", 40),
            ("Hermmann", "X", 50),
            ("Patrick", "Y", 22),
            ("Sebastian", "A", 34))

student_age = lambda age: age[2]
sorted_students = sorted(students, key=student_age)
for i in sorted_students:
    print(i)
