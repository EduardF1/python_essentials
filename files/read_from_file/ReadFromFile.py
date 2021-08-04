# Example of opening and reading a file (line by line)

try:
    with open('resources/test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('The specified file was not found.')

#   print(file.closed)

# Note: With this approach, the file will be automatically closed after being read
#       , for testing purposes, we print the value of the `closed` property (True).
#       However, this will not catch exceptions (if any).
#       Usually, files need to be closed after being read.
