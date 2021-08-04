# dictionary = a changeable (mutable), unordered collection of unique key:value pairs
#              Fast because it uses hashing, allowing fast access to a value

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# A not so-safe way of accessing dictionary elements (if the key is nonexistent, an error is thrown)
# print(capitals['USA'])

# better alternative (returns `None` if the element is not present in the dictionary)
# print(capitals.get('Germany'))

# print all the dictionary keys
# print(capitals.keys())

# print all dictionary values
# print(capitals.values())

# print all dictionary items
# print(capitals.items())

# add items to the dictionary using the update() function
# capitals.update({'Germany': 'Berlin'})

# update the value of an item
# capitals.update({'USA': 'Las Vegas'})

# remove a specified item through its key from the dictionary
# capitals.pop('China')

# remove all elements from the dictionary
# capitals.clear()

# print each key-value pair
for key, value in capitals.items():
    print(key, value)
