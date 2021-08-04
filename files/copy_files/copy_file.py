# functions to copy a file:
# 1) copyFile() =   copies file contents
# 2) copy() =   copyFile() + permission mode + destination (can be a directory)
# 3) copy2() =  copy() + copies metadata (file creation and modification times)

import shutil

shutil.copyfile('test.txt', 'copy.txt')  # args: src, dest

# Note: dest - can be specified as absolute path for copying a file to i.e. the desktop
