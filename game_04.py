# Forth version of the game.
# For loop and break statement.

print("*******************")
print("Welcome to my game!")
print("*******************")

secret_number = 42
total_guesses = 3


for round in range(1, total_guesses + 1):
	# instead of using an iterator variable, in Python it's preferred to
	# use the range() function to go over an array's indexes.
	# range() function will deal with a range of values. Its first parameter
	# is the value to start with and the second is the value to stop (it will
	# exclude this value on the final array) and the third is the step size
	# (how many elements will be added to the iterator on each loop). Note
	# that all the parameters are optional: the first one can be anything, but
	# the other two are optional.
	# It's important to notice that the second parameter of range() will never
	# be included on the array. Thus, range(1, 3) will yield (1, 2). so we need
	# to add one to the total_guesses, otherwise round will only go from 1 to 2.
	print("Try #{} of {}".format(round, total_guesses))

	guess_str = input("Please, type a random number: ")
	guess_int = int(guess_str)
	win = guess_int == secret_number
	higher = guess_int > secret_number
	lower = guess_int < secret_number

	print("You guessed:", guess_str)
	if win:
		print("YOU WIN!")
		break
	# The break statement will immediately stop the loop execution. If you
	# don't use it, Python will continue to iterate over the guesses even
	# though the user already won. It's important to use break only in loops
	# when you know that you have succeeded, otherwise it can lead to larger
	# problems.
	# Same as C.
	else:
		if higher:
			print("You lost. This number is higher than the secret number!")
		elif lower:
			print("You lost. This number is lower than the secret number!")

