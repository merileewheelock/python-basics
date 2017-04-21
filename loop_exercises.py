#1 to 10
for i in range(11):
	print i

#n to m
start = int(raw_input("Start from: "))
end = int(raw_input("End on: "))
for i in range(start, end + 1):
	print i

#Odd Numbers
for i in range(1,10,2):
	print i

#Print a Square
stars = "*"
for i in range(5):
	print stars * 5

#Print a Square II
num_stars = int(raw_input("How big is the square? "))
for i in range(num_stars):
	print "*" * num_stars

#Print a box
blank = " "
width = int(raw_input("Width? "))
height = int(raw_input("Height? "))
for i in range(height):
	if i == 0:
		print "*" * width
	print "*" + (blank * (width - 2)) + "*" 
	if i == height - 1:
		print "*" * width

#Print a Triangle
star = "*"
blank = " "
r = int(raw_input("Height? "))
for i in range (1, r + 1):
	number_of_spaces = (2 * (r - i)) / 2
	number_of_stars = 1 + (2 * (i - 1))
	print (number_of_spaces * blank + number_of_stars * star)

# Multiplication Table
total = 0
for i in range(1,11):
	for j in range(1,11):
		both = int(i * j)
		total = "%d x %d = %d" % (i, j, both)
		print total

#Print A Banner
text = raw_input("Enter some text. ")
for i in text:
	print (len(text) * "*") + "**"
	print "*" + text + "*"
	print (len(text) * "*") + "**"
	break

#Triangle Numbers


#Factor A Number


