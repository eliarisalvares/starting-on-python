# The fifth version of the game.
# Using 'continue' statement on a loop with nested ifs to check the user's
# hints and "or" boolean operator. Generate a random number using the
# 'random' library.

# Unlike the functions we have been using so far in these exercises, random()
# does not belong to the standard Python installation, so we need to import it.
# Equivalent to #include in C.
import random

print("*******************")
print("Welcome to my game!")
print("*******************")

# random.random() returns a random floating point number between 0 and 1, this
# 0 is inclusive while 1 is exclusive. If this was our choice, we could use it
# to generate a random floating point number, cast it to integer and multiply
# by 100. random.randrange() might be a more appropriate function in this case,
# since it will give integers between a minimum and maximum range.
# Using random.random() we can also cast the result to integer using the
# function round() to get an integer instead of int().
# Called with only one parameter, random.randrange() will assume that we want
# random numbers ranging from 0 to the integer passed as parameter.
secret_number = random.randrange(0, 100)
total_guesses = 3


for round in range(1, total_guesses + 1):
	print("Try #{} of {}".format(round, total_guesses))

	guess_str = input("Please, type a random number between 1 and 100: ")
	guess_int = int(guess_str)

	# In Python, the "and" and "or" operators can be used to enhance boolean
	# expressions. Their behavior is like C's, but with the literal words
	# instead of with the "&&" and "||" from C.
	if (guess_int < 1 or guess_int > 100):
		print("You must type a random number between 1 and 100!")
		continue

	# Like in C, the continue statement will stop the current iteration and
	# jump to the beginning of the loop

	win = guess_int == secret_number
	higher = guess_int < secret_number
	lower = guess_int > secret_number

	print("You guessed:", guess_str)
	if win:
		print("YOU WIN!")
		break
	else:
		if higher:
			print("You lost. This number is higher than the secret number!")
		elif lower:
			print("You lost. This number is lower than the secret number!")

# There are no true random number generators, only pseudo-random number
# generators. The random() function uses a seed number to generate a sequence
# of apparently random numbers. We can force a seed using the seed() method
# from the random module. If we choose the same seed numbers, random() will
# return the same sequence of numbers.
