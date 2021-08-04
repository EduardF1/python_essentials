# set = collection, unordered,unindexed with no duplicate values.
# faster than lists
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# set utility methods

# add an item to the set
# utensils.add("napkin")

# remove a specific element within the set
# utensils.remove("fork")

# remove all set elements
# utensils.clear()

# add a set (specified argument) to the referenced set (concatenate sets)
# utensils.update(dishes)

# join two sets into a completely new set
# dinner_table = utensils.union(dishes)

# set difference / A: {a,b,c}, B: {a,b} -> A - B = {c}
# print(utensils.difference(dishes))
# print(dishes.difference(utensils))

# set intersection / A: {a,b,c}, B: {a,b} -> A ∩ B = {a,b}
# print(dishes.intersection(utensils))

# print all elements in utensils
# for x in utensils:
#    print(x)
