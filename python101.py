print "Hello, World!"

Print two different things on the same line
print ("Hello, World", "Again")

print """This
will ignore the new lines
until it sees another 
three double quotes""" 

print "Another line"


# Variables - string, number, letters, any other stuff made with keyboard
# and you want to stash something that is not fast into something that is fast
# There is no declaration for a variable.
name = "Merilee Wheelock" #semicolon is optional
# Python is not heavily typed

Arithmatic
print int(30.5 / 4.2) #The deimal usually returns a declimal, int() returns an integer
Cannot add an integer and a string

Data types (variable types)
-strings
-numbers: floats, integers (use integers when you can, only floats when you have to)
-booleans: true of false
-lists: list of variables
-dictionary: variables of variables
-objects

first_name = "Merilee"
last_name = "Wheelock"
print "Hello, {} {}".format(first_name, last_name)

#Placeholders
print "Hello, %s %s " % (first_name, last_name)
print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)

#Floats
pi_the_magic_float = 3.14
print pi_the_magic_float
print type(pi_the_magic_float)
make_me_an_integer = int(pi_the_magic_float)
print make_me_an_integer
int() to make an integer
str() to make a string

Booleans - true or false
True and False are uppercase
the_truth = True
print type(the_truth)
the_lie = False
print type(the_lie)

Raw Input
first_name = raw_input("First Name: ")
last_name = raw_input("Last Name: ")
#Whatever the user enters will be assigned to first_name

#Conditionals
# 1 = means you want to assign something
# 2 == means you want to compare the thing on the left to the thing on the right

if (first_name == last_name):
	print "Your first name is the same as your last name?"

#If you want to compare = or greater than, >=
age  = raw_input("How old are you? ") #Raw input comes back as a string
age_as_int = int(age)
#print type(age) Comes back as a string
if (age_as_int >= 21):
	print "You can buy beer!"
else:
	print "You are underage."

#Random number generator
import random
random_number = random.randint(1,10)
# print random_number

#Loop - keep doing something until I tell you to stop
not_guessed = True
while not_guessed:
	guess_a_number = raw_input("Guess a number between 1 and 10. ")
	if (int(guess_a_number) == random_number):
		print "You guessed the number!"
		not_guessed = False


list is a single variable with a bunch of numbered parts
the number that an element is in is called the "Index"
lists start at index 0

students = [
	"Marissa",
	"Merilee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stephen",
	"Drew"
]
print (students[1])
print (students[-1]) # will start at the last item in the array

atlantaTeams = [
	"Falcons",
	"Braves",
	"Hawks",
	"Thrashers"
]

print atlantaTeams

# To add an element to the END of the list, you can use the append method
atlantaTeams.append("Atlanta United")
print atlantaTeams

# Pop REMOVES the last item on the list
atlantaTeams.pop()
print atlantaTeams

# To delete an index, you can use the remove method
atlantaTeams.remove("Thrashers")
print atlantaTeams

# We can insert into any indicie with the insert method
atlantaTeams.insert(0, "Georgia Tech")
print atlantaTeams

# Split - When we run into some indicator, a new element in the list will be created
teams_as_a_string = "Falcons, Braves, Hawks, Thrashers"
print teams_as_a_string
teams_as_a_list = teams_as_a_string.split(",")
print teams_as_a_list

# sort() will sort in alphabetical order
# sort will CHANGE the list
# atlantaTeams.sort();
# print atlantaTeams

# sorted() will sort but NOT CHANGE the list
copy_of_atlanta_teams = sorted(atlantaTeams)
print copy_of_atlanta_teams

copy_of_atlanta_teams.reverse()
print copy_of_atlanta_teams

length_of_atlanta_teams = len(copy_of_atlanta_teams) #this gives the length of indices
print length_of_atlanta_teams
print copy_of_atlanta_teams[-1]
print copy_of_atlanta_teams[length_of_atlanta_teams - 1] #this gives the last item in the index


If you want a portion of a list, you can use the [x:y] format.
This will create a COPY fo the array, does not mutate or change the original.
It will start at the Xth element and fo to the Yth element.

students = [
	"Marissa",
	"Merilee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stephen",
	"Drew"
]

print students
second_and_third = students[1:3] #exclusive of 3
print second_and_third
all_but_the_first = students[1:]
print all_but_the_first


FOR LOOP
i stands for index/increment
for i in range(1,10): #prints 1 through 9 (not inclusive of 10)
	print i

students = [
	"Marissa",
	"Merilee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stephen",
	"Drew"
]

For Loop Format:
[for] [what_you_want_to_call_the_thing_you_are_on] [in] [variable_looping_through]


for student in students:
	#print student
	if (student == "Chris"):
		print "Welcome, Chris!"
	else:
		print "You are not Chris."

Set up a for loop... but the range will be 0 to len-1
students_length = len(students)
for i in range(0, students_length): #don't need -1 because the last number in the range is not inclusive
	print students[i]

for i in range(0,10,2): #the "2" at the end is a "step", so increments by 2
	print i


FUNCTIONS
A function is a piece of code that can be called form the main body of the program.
The upshot is that if you have complicated code or code that is repeted often, function is your answer.
Repeating yourself is BAD.
A function in python is not a function, it is a definition.
To declare a function in python, you use "def".
Functions always have parentheses ().

def say_hello():
	print ("Hello")

say_hello() #This calls the function

def say_hello_with_name(name): 		#name is a parameter; this is a local variable
	print ("Hello, " + name)

# say_hello_with_name() #this will fail due to no parameters
# say_hello_with_name("Rob", "Chad") # this will fail because too many parameters

say_hello_with_name("Nick")

def say_hello_with_default(name, in_class = "Yes"):
	print ("Hello, " + name)
	print "Is student in class? " + in_class

say_hello_with_default("Carla") #second variable is not provided, so will use default in_class = "Yes"
say_hello_with_default("Max", "No")

#Functions always return something
def return_user_name(name):
	return name

print return_user_name("YingRong")

def make_uppercase(string):
	return string.upper()

normalized_string = make_uppercase("I'm  wIlD ANd craZY GuY")
print normalized_string


