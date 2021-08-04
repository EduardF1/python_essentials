# filter() =    creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)
# can be though of as `list of results` for a specified criteria

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Joel", 17),
           ("Davis", 29),
           ("Karl", 31),
           ("Ross", 20)]

age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
