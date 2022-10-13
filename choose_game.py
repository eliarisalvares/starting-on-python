# when importing files from other directories, unlike C, in Python 3, we should
# use the "from" ... "import" syntax instead of relative paths
from guessing_game import guessing_game
#from hangman_game import hangman_game
import time

def choose_game():
	print("*******************")
	print("Choose game to play")
	print("*******************")

	print("Type 1 to play the guessing game!")
	print("Type 2 to play hangman game!")
	chosen_game = int(input("Which game would you like to play: (1) or (2)?"))

	if chosen_game == 1:
		print("Starting guessing game...")
		guessing_game.guessing_game()
	# elif chosen_game == 2:
	#	print("Starting hangman game...")
	#	hangman_game.hangman_game()
	else:
		print("No corresponding game. Try again.")
		time.sleep(2)

if __name__ == "__main__":
	choose_game()
