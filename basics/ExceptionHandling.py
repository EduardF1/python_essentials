# exception =   events detected during execution that interrupt the (normal) flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator

# specific exception handling, handle attempts to divide by `0`
except ZeroDivisionError as e:
    print(e)
    print("Division by 0 is not possible, revise your understanding of division.")

# handle incompatible type division
except ValueError as e:
    print(e)
    print("Enter only numbers please.")

# generic exception handling (handles all exceptions, unanticipated, considered to not be best practice)
except Exception as e:
    print(e)
    print("Something went wrong :-<")

# if no exception occurred, print the result
else:
    print(result)

# An use case for the `finally` clause is to close opened resource files
finally:
    print('This will always execute.')

