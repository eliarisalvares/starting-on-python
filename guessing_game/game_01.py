# first version of the game.
# variables declaration and comparison - basic Python syntax

print("*******************")
print("Welcome to my game!")
print("*******************")

secret_number = 42

# the input() function returns a string, it waits user input from standard
# input (the terminal) and reads the user input when enter is pressed.
guess = input("Please, guess number: ")
print("You guessed: ", guess)

# if conditions and other statements/executions use the final ":" and
# line indentations in Python instead of parentheses and curly brackets, like
# in other programming languages.
""" if guess == secret_number:
	print("YOU WIN!")
else:
	print("Sorry, you lost!")
	print("Better luck next time.")
 """

# we need to explicitly cast the string variable to integer, otherwise,
# we won't be able to perform a comparison operation
# int() function is used to explicit perform the cast.
if int(guess) == secret_number:
	print("YOU WIN!")
else:
	print("Sorry, you lost!")
	print("Better luck next time.")

#Another possibility would be to explicitly cast the secret number in its
# declaration to integer:
"""
secret_number = int(42)
"""
