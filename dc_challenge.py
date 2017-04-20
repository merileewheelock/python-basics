# 1) Declare two variables, a strig and an integer
# named "fullName" and "age". Set them equal to your name and age.

full_name = "Merilee Wheelock"
age = 27



#There are no arrays, but there are lists. Not push, append.
my_array = []
my_array.append(full_name)
my_array.append(age)
print my_array




def say_hello():
	print "Hello!"

say_hello()


# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed in the instructions PDF.

split_name = full_name.split()
print split_name


# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)

def say_name():
	print ("Hello, " + split_name[0])

say_name()


# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.
# HINT: http://www.w3schools.com/js/js_functions.asp

def my_age(birthyear):
	print (2017 - birthyear)

my_age(1989)


# 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console the sum of all the odd numbers from 1 to 5000.  Don't forget to call the function!
# HINT: Consider using a 'for loop'.

def sum_odd_numbers():
	sum = 0
	for i in range(1,5001,2):	#2 is the step (increases by 2)
		sum += i
	return sum

print sum_odd_numbers()


# def sum_odd_numbers():
# 	sum = 0
# 	for i in range(1,5001):
# 		if (i % 2 == 1):	#This uses the modulus instead of the step
# 		 sum += i
# 	return sum

# print sum_odd_numbers()

i = 0
while 1:	#this alone will run forever
	i += 1
	print i
	if (i ==10):
		break
print "We broke out of the loop!"