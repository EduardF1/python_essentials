import os
import shutil

paths = ['test.txt', 'empty_directory', 'directory']


def create_empty_directory():
    if not os.path.exists('empty_directory'):
        os.makedirs('empty_directory')


def create_test_file():
    if not os.path.exists('test.txt'):
        text = "A file to be deleted."
        with open('test.txt', 'w') as file:
            file.write(text)


def create_directory_with_test_file():
    if not os.path.exists('directory'):
        os.makedirs('directory')
        if not os.path.exists('test2.txt'):
            text = "A file to be deleted."
            with open('directory/test2.txt', 'w') as file:
                file.write(text)


def set_resources():
    create_empty_directory()
    create_test_file()
    create_directory_with_test_file()


try:
    set_resources()

    os.remove(paths[0])  # remove a file
    os.rmdir(paths[1])  # remove a directory (empty)
    shutil.rmtree(paths[2])  # remove a directory and all its children (!empty)

except FileNotFoundError:
    print('The specified file was not found')
except PermissionError:
    print('You do not have permission to delete the specified resource')
except OSError:
    print('You cannot delete the specified resource with the current function')
else:
    for i in paths:
        print(i + " was deleted")
