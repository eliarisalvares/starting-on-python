import random

# in Python, functions are defined using the 'def' reserved word. To declare a
# function without any parameter, as is the case here, add the "()" without
# any argument inside. Then, just like when using if, for or while, end of the
# function definition must be defined with a colon, ":" and following lines
# must be idented with 4 spaces ("tab").
def guessing_game():

	print("****************************")
	print("Welcome to my guessing game!")
	print("****************************")

	secret_number = random.randrange(0, 100)
	total_guesses = 10
	points = 1000

	print("Choose a level to play: (1) Beginner, (2) Normal, (3) Professional")
	level = int(input("Please, type 1, 2 or 3: "))
	if level != 1 and level != 2 and level != 3:
		print("Invalid level. The default level will be (2) Normal.")

	if level == 1:
		total_guesses = 20
	elif level == 2:
		total_guesses = 10
	else:
		total_guesses = 5

	for round in range(1, total_guesses + 1):
		print("Try #{} of {}".format(round, total_guesses))

		guess_str = input("Please, type a random number between 1 and 100: ")
		guess_int = int(guess_str)

		if (guess_int < 1 or guess_int > 100):
			print("You must type a random number between 1 and 100!")
			continue

		win = guess_int == secret_number
		higher = guess_int > secret_number

		print("You guessed:", guess_str)
		if win:
			print("YOU WIN!")
			print("The secret number was:", secret_number)
			print("Your total score is {}".format(points))
			break
		else:
			if higher:
				print("You lost. This number is higher than the secret number!")
			else:
				print("You lost. This number is lower than the secret number!")
		if round == total_guesses:
			print("GAME OVER")
			break
		lost_points = abs(secret_number - guess_int)
		points -= lost_points

