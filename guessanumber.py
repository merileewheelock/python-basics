# secret_number = 5
# not_guessed = True
# while not_guessed:
# 	print "I am thinking of a number between 1 and 10."
# 	guess_a_number = raw_input("What's the number? ")
# 	if int(guess_a_number) == secret_number:
# 		not_guessed = False
# 		print "Yes! You win!"
# 	else:
# 		print "Nope try again."


# secret_number = 5
# not_guessed = True
# while not_guessed:
# 	print "I am thinking of a number between 1 and 10."
# 	guess_a_number = raw_input("What's the number? ")
# 	if (int(guess_a_number) == secret_number):
# 		not_guessed = False
# 		print "Yes! You win!"
# 	elif (int(guess_a_number) < secret_number):
# 		print "%d is too low." % int(guess_a_number)
# 	elif (int(guess_a_number) > secret_number):
# 		print "%d is too high." % int(guess_a_number)


secret_number = 5
not_guessed = True
attempts = 5
while not_guessed:
	print "I am thinking of a number between 1 and 10."
	guess_a_number = raw_input("What's the number? ")
	if int(guess_a_number) == secret_number:
		not_guessed = False
		print "Yes! You win!"
	elif int(guess_a_number) < secret_number:
		print "%d is too low. You have %d guesses left." % (int(guess_a_number), attempts)
		#attempts -= 1
	elif int(guess_a_number) > secret_number:
		print "%d is too high. You have %d guesses left." % (int(guess_a_number), attempts)
		#attempts -= 1
	attempts -= 1
	if attempts == 0:
		not_guessed = False
		print "You ran out of guesses!"
		play_again = raw_input("Do you want to play again (Y or N)? ")
		if play_again == "Y":
			not_guessed = True
			attempts = 5
		elif play_again == "N":
			print "Bye!"
