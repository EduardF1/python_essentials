# logical operators (and, or, not). Usage: check if 2+ conditional statements are true

temp = int(input('What is the temperature outside?:'))

# temp: (-inf.,0) U (30,+ inf)
if not (temp >= 0 and temp <= 30):
    print('The temperature is good today.')
    print('Go outside for a walk...')
# temp: [0,30]
elif not(temp < 0 or temp > 30):
    print('The temperature is quite bad today')
    print('Stay inside...')
