class Vehicle:
	
	default_color = 'grey'
	number_of_vehicles = 0

	def __init__(self, modele, color):
		self.color = color
		self.modele = modele
		Vehicle.number_of_vehicles += 1

	def full_name(self):
		return('This is a {} {}.'.format(self.color, self.modele))

	def change_color(self):
		self.color = Vehicle.default_color

	@classmethod
	def change_default_color(cls, color):
		cls.default_color = color

	@classmethod
	def from_string(cls, str): # alternate constructors starts with 'from_'. It's a convention.
		color, modele = str.split('-')
		return cls(color, modele)

	@staticmethod # a static method is nothing more than a function defined inside a class. It is callable without instantiating the class first.
	def is_work_day(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


print(Vehicle.number_of_vehicles)

a = Vehicle('Renault', 'red')
b = Vehicle('Peugeot', 'blue')

print(Vehicle.number_of_vehicles)

print(a.full_name())
a.change_color()
print(a.full_name())
print(a.__dict__)
print(Vehicle.__dict__)
b.default_color = 'green' # Doesn't change the value of the Class variable but create a new attribute for b.
print(a.__dict__)
print(b.__dict__)
print(Vehicle.default_color)
Vehicle.change_default_color("yellow") # We call a class method to change the value of a class attribute.
print(Vehicle.default_color)
b.change_color()
print(b.__dict__)

c = Vehicle.from_string("black-Ford") #the class method 'from_string' is an alternate constructor
print(c.__dict__)

import datetime
my_date = datetime.date(2017, 2, 5)

print(Vehicle.is_work_day(my_date))