class Car:
    def __init__(self, name, year, hp):
        self.name = name
        self.year = year
        self.hp = hp

    def print_my_car(self):
        print("The name of my car is: ", self.name, ".")

my_car = Car("Audi A1 Sportback 40 TFSI", "2020", "200")
my_car.print_my_car()