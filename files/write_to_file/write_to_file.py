# Note: the open function takes as arguments the file path and mode (`a` - append, `w` - write, `r` - read)

text = "\nSee ya, wouldn't want to be ya."
with open('test.txt', 'a') as file:
    file.write(text)

