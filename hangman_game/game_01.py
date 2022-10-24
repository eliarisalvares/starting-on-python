def	hangman_game():
	print("*******************")
	print("Welcome to hangman!")
	print("*******************")

	secret_word = "banana"

	# True and False with capital T and F are used in Python when dealing with
	# booleans. This is because True and False are values instead of keywords
	hanged = False
	won = False

	# instead of "!", the "not" in Python is used for negation
	# keywords in Python are lowercase (and, or, not)
	while(not hanged and not won):
		guessed_letter = input("Type the letter: ")
		# to check whether a character is in a word, it would be possible to use
		# the find() function and check for != -1 return value. However, this
		# won't be the chosen path as Python has a keyword with better
		# readability, the "in" keyword.
		guessed_letter = guessed_letter.strip()
		# strip() removes the whitespace from the beginning and end of a string

		i = 0
		for letter in secret_word:
			if (guessed_letter.upper() == letter.upper()):
				print("Congrats! Letter {}".format(guessed_letter), end="")
				print(" is in the secret word at position {}.".format(i))
			i += 1

if (__name__ == "__main__"):
	hangman_game()
