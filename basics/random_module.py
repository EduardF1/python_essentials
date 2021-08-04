import random

x = random.randint(1, 6)  # generate a pseudo-random (int) number in [1,6]
y = random.random()  # generate a pseudo-random (float) number

optionList = ['rock', 'paper', 'scissors']
z = random.choice(optionList)  # choose a random value from a specified collection/sequence

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)   # shuffle the items of a collection

print(cards)
