class Animal:
    alive: bool = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping.")


class Rabbit(Animal):
    def run(self):
        print("The rabbit is running.")


class Hawk(Animal):
    def fly(self):
        print("The hawk if flying.")


class Fish(Animal):
    def swim(self):
        print("The fish is swimming.")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
fish.swim()
hawk.fly()
rabbit.run()