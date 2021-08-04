import os

source = "test_directory"  # move an entire directory
# source = "text.txt"  # move a file
destination = "C:\\Users\\fisch\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        os.replace(destination, source)
        print(destination + " was moved.")
    else:
        os.replace(source, destination)
        print(source + " was moved.")
except FileNotFoundError:
    print(source + " was not found.")
