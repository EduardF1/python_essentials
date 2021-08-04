# tuple = a collection which is ordered and unchangeable
#         used to group together related data

student = ("Mike", 21, "male")

# print number_of_occurrences for `Mike`
print(student.count("Mike"))
# print index_of for `male`
print(student.index("male"))

for x in student:
    print(x, end=" ")
if "Mike" in student:
    print("\nMike is here.")
