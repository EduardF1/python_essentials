import os

# path to file directory, for file add `\\test.txt`
path = "C:\\Users\\fisch\\Desktop\\test"

if os.path.exists(path):
    print('The specified location exists')
    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print('That is a directory')
else:
    print('The specified location does not exist')
