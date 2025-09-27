class Car:
    def __int__(self, make="", model="", year="", color="", mileage=0):
        self.make = make
        self.model = model
        self.year =  year
        self.color = color
        self.mileage = mileage

    def print_car_info(self):
        print(f"Car Info: {self.year} {self.color} {self.make} {self.model}, Mileage: {self.mileage}")

class SportsCar(Car):

    def __init__(self, make, model, year, color, mileage, top_speed=0):
        super().__int__(make, model, year, color, mileage)
        self.top_speed = top_speed

    def print_car_info(self):
        super().print_car_info()
        print(f"Top Speed: {self.top_speed} mph")
        print(f"Make: {self.make}")

my_car = SportsCar("Toyota", "Camry", 2019, "Red", 0, 155)


my_car.print_car_info()