class Person(object):	#have to pass the object right away in Python
	def __init__(self, name, gender, number_of_arms, cell):		#always pass self, name is optional
		self.name = name
		self.gender = gender #these don't have to be the same but often make the same
		self.species = "Human" #all Persons are automatically set to human
		self.number_of_arms = number_of_arms
		self.phone = {
			"cell": cell,
			"home": "Who has a home phone anymore?"
		}

	def greet(self, other_person):
		print "Hello %s, I am %s!" % (other_person, self.name)

	def print_contact_info(self):
		if (self.phone["cell"] != ""):
			print "%s's number is %s" % (self.name, self.phone["cell"])

marissa = Person("Marissa", "female", 3, "770-777-7777")	#self is always implied, don't pass self
print marissa.name, marissa.gender, marissa.species, marissa.number_of_arms

merilee = Person("Merilee", "female", 2, "770-555-5555")
print merilee.species	#this will return Human
merilee.species = "Robot"
print merilee.species	#this will return Robot due to reassigning .species to robot
print merilee.number_of_arms
print marissa.phone["cell"]
print marissa.phone["home"]

marissa.greet("Rob")
marissa.print_contact_info()		#This will run the code
print merilee.print_contact_info	#This will not error but will print the actual method



class Vehicle(object):
	def __init__(self, make2, model2, year2):
		self.make = make2	#2 added to make clearer
		self.model = model2
		self.year = year2

	def print_info(self):
		print self.year, self.model, self.make

	def change_year(self, new_year):
		self.year = new_year

	def get_year(self):
		return self.year

david_cummings_car = Vehicle("Mcclaren", "Mp4-12c", 2013)
david_cummings_car.print_info()

david_cummings_car.change_year(2015)	#These two are the same
david_cummings_car.year = 2015

print david_cummings_car.year			#These two are the same
print david_cummings_car.get_year()



