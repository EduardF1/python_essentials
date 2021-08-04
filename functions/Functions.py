# function = a block of code which is executed only when it is called

first_names = {'Person_1': 'Kyle', 'Person_2': 'Joshua', 'Person_3': 'Nathan'}
last_names = {'Person_1': 'McCain', 'Person_2': 'Fluke', 'Person_3': 'DeOmbargo'}
ages = [22, 33, 44]


def hello(first_name: str, age: int, last_name: str):
    print('Hello ' + first_name + ' ' + last_name + '\n' + 'You are: ' + str(age) + ' old.')
    print('Have a nice day.\n')


hello(first_names.get('Person_1'), ages[0], last_names.get('Person_1'))
hello(first_names.get('Person_2'), ages[1], last_names.get('Person_2'))
hello(first_names.get('Person_3'), ages[2], last_names.get('Person_3'))
