# slicing = create a substring by extracting elements from another string
#           indexing[] op. or slice() func.
#           [start:stop:step]

name = 'Charles Bronson'
#first_name = name[0:6] # Output: `Charle`, the stop index is not inclusive
#first_name = name[:7]  # Py. assumes the first value is `0`
first_name = name[0:7:1]
print(first_name)

#last_name=name[8:15]
last_name=name[8:]
print(last_name)

#weird_name = name[0:7:3]
weird_name = name[::3] # left out start (assumed to be 0) and left out end (assumed to be the last index)
print(weird_name)

reversed_name = name[::-1]
print(reversed_name)

# each index has a + value and a - value (`m` is -1)
website_url1 = "https://reddit.com"
website_url2 = "https://wikipedia.com"

slice = slice(8, -4)
print(website_url1[slice])
print(website_url2[slice])
