# #1 Hello you
# name = raw_input("What is your name? ")
# print "Hello, " + name + "!"

# #2 HELLO YOU!
# name = raw_input("WHAT IS YOUR NAME? ")
# print "HELLO, " + name.upper() + "! YOUR NAME HAS %d LETTERS IN IT! AWESOME!" % len(name)

# #3 Madlib
# print "Please fill in these blanks: ___'s favorite band is ___."
# name = raw_input("What is your name? ")
# band = raw_input("What is your favorite band? ")
# print "%s's favorite band is %s." % (name, band)

# #4 Day of the Week
# day = int(raw_input("Day (0-6)? "))
# days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# print days_of_week[day]


# #5 Work or Sleep In
# day = int(raw_input("Day (0-6)? "))
# if day == 0 or day == 6:
# 	print "Sleep in"
# if day >= 1 and day <= 5:
# 	print "Go to work"

# #6 C to F
# temp_in_C = raw_input("Temperature in C? ")
# conv_to_F = int(temp_in_C) * 1.8 + 32
# print "%d F" % conv_to_F

# #7 Tip Calculator
# subtotal = raw_input("Total bill amount? $")
# service = raw_input("Level of service? (good, fair, or bad) ")
# if service == "good":
# 	total = int(subtotal) + (int(subtotal) * .20)
# 	print "Total amount: $%d" % total
# if service == "fair":
# 	total = int(subtotal) + (int(subtotal) * .15)
# 	print "Total amount: $%d" % total
# if service == "bad":
# 	total = int(subtotal) + (int(subtotal) * .10)
# 	print "Total amount: $%d" % total

# #8 Tip Calculator
# subtotal = raw_input("Total bill amount? $")
# service = raw_input("Level of service? (good, fair, or bad) ")
# split = raw_input("Split how many ways? ")
# if service == "good":
# 	total = (int(subtotal) + (int(subtotal) * .20)) / int(split)
# 	print "Total amount: $%d" % total
# if service == "fair":
# 	total = (int(subtotal) + (int(subtotal) * .15)) / int(split)
# 	print "Total amount: $%d" % total
# if service == "bad":
# 	total = (int(subtotal) + (int(subtotal) * .10)) / int(split)
# 	print "Total amount: $%d" % total

# #9 1 to 10
# count = 1
# while (count <= 10):
# 	print count
# 	count = count + 1

# #10 How many coins?
# coin_count = 0
# keep_going = True
# while keep_going:
# 	response = raw_input("You have %d coins. Do you want another? (yes/no) " % coin_count)
# 	if response == "yes":
# 		coin_count = coin_count + 1
# 		keep_going = True
# 	if response == "no":
# 		print "Bye"
# 		keep_going = False

