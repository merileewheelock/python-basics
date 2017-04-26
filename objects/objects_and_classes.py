
# Basics
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    #Add a method 2
	def print_contact_info(self):
		print "Sonny's email: %s, Sonny's phone number: %s" % (self.email, self.phone)

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
print sonny.name, sonny.email, sonny.phone

# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
print jordan.name, jordan.email, jordan.phone

# Have sonny greet jordan using the greet method.
print sonny.greet(jordan)

# Have jordan greet sonny using the greet method.
print jordan.greet(sonny)

# Write a print statement to print the contact info (email and phone) of Sonny.
print sonny.email, sonny.phone

# Write another print statement to print the contact info of Jordan.
print jordan.email, jordan.phone

# sonny.print_contact_info()

# Make your own class
class Vehicle(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	
	#Add a method
	def print_info(self):
		print car.year, car.make, car.model

car = Vehicle('Nissan', 'Leaf', 2015) 
print car.make, car.model, car.year
car.print_info()

