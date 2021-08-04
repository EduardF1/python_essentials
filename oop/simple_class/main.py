from car import Car

# self does not need to be passed to the constructor
car_1 = Car("Chevrolet", "Camaro", 2021, "red")
car_2 = Car("Ford", "Mustang", 1967, "blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()