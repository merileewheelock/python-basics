# print "Hello, World!"

# Print two different things on the same line
# print ("Hello, World", "Again")

# print """This
# will ignore the new lines
# until it sees another 
# three double quotes""" 

# print "Another line"


# # Variables - string, number, letters, any other stuff made with keyboard
# # and you want to stash something that is not fast into something that is fast
# # There is no declaration for a variable.
# name = "Merilee Wheelock" #semicolon is optional
# # Python is not heavily typed

# Arithmatic
# print int(30.5 / 4.2) #The deimal usually returns a declimal, int() returns an integer
#Cannot add an integer and a string

# Data types (variable types)
# -strings
# -numbers: floats, integers (use integers when you can, only floats when you have to)
# -booleans: true of false
# -lists: list of variables
# -dictionary: variables of variables
# -objects

# first_name = "Merilee"
# last_name = "Wheelock"
# print "Hello, {} {}".format(first_name, last_name)

# #Placeholders
# print "Hello, %s %s " % (first_name, last_name)
# print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)

# #Floats
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer
# int() to make an integer
# str() to make a string

#Booleans - true or false
#True and False are uppercase
# the_truth = True
# print type(the_truth)
# the_lie = False
# print type(the_lie)

# Raw Input
# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")
# #Whatever the user enters will be assigned to first_name

# #Conditionals
# # 1 = means you want to assign something
# # 2 == means you want to compare the thing on the left to the thing on the right

# if (first_name == last_name):
# 	print "Your first name is the same as your last name?"

# #If you want to compare = or greater than, >=
# age  = raw_input("How old are you? ") #Raw input comes back as a string
# age_as_int = int(age)
# #print type(age) Comes back as a string
# if (age_as_int >= 21):
# 	print "You can buy beer!"
# else:
# 	print "You are underage."

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