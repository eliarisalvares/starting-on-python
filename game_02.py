# Second version of the game.
# Elif statement, code readability.

print("*******************")
print("Welcome to my game!")
print("*******************")

secret_number = 42
guess_str = input("Please, guess number: ")
guess_int = int(guess_str)

print("You guessed: ", guess_str)
# Unlike C, Python uses the "elif" keyword instead of the "else if".

""" if guess_int == secret_number:
	print("YOU WIN!")
else:
	if guess_int < secret_number:
		print("You lost. This number is higher than the secret number!")
	elif guess_int > secret_number:
		print("You lost. This number is lower than the secret number!") """

# To improve code readability, we can insert this conditions into variables.

win = guess_int == secret_number
higher = guess_int < secret_number
lower = guess_int > secret_number

if win:
	print("YOU WIN!")
else:
	if higher:
		print("You lost. This number is higher than the secret number!")
	elif lower:
		print("You lost. This number is lower than the secret number!")

