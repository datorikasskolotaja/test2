class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
	
    def drive(self):
        return f"{self.brand} {self.model} brauc!"

car1 = Car("Toyota", "Corolla")
print(car1.drive())