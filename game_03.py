print("*******************")
print("Welcome to my game!")
print("*******************")

secret_number = 42
total_tries = 3
round = 1

while round <= total_tries:
	# print("Try #", round, "of", total_tries)

	# Unlike C, Python uses the "format" method for printf-like functionality
	# and {} as the placeholder for string interpolation.
	print("Try #{} of {}".format(round, total_tries))

	guess_str = input("Please, type a random number: ")
	guess_int = int(guess_str)
	win = guess_int == secret_number
	higher = guess_int < secret_number
	lower = guess_int > secret_number

	print("You guessed:", guess_str)
	if win:
		print("YOU WIN!")
	else:
		if higher:
			print("You lost. This number is higher than the secret number!")
		elif lower:
			print("You lost. This number is lower than the secret number!")
	round += 1

