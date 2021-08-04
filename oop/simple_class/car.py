class Car:

    # initialize function (`constructor`), the self argument is the obj. reference
    def __init__(self, make, model, year, color):
        # class attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # class methods
    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")
