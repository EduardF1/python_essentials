# reduce() =    apply a function to an iterable and reduce it to a single cumulative value.
#               performs the specified function on the first two elements and repeats the process until 1 value remains
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
# 1) ["HE", "L", "L", "O"] -> 2) ["HEL", "L", "O"] -> 3) ["HELL", "O"] -> 4) ["HELLO"] -> exit
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
# 1) [20, 3, 2 ,1] -> 2) [60, 2,1] -> 3) [120, 1] -> 4) [120] -> exit
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
