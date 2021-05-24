import random
import time #loading delay


name = input("Please Enter your name for the Game ")
print("Welcome" ,name, "to the Hangman Game!\nGood Luck ! ")
time.sleep(1)

words = ['subway', 'awkward', 'jogging', 'funny',
		'python', 'oxygen', 'puppy', 'cobweb',
		'reverse', 'stretch ', 'rhythm', 'zigzag']

# random words from the words list
word = random.choice(words)

print("Guess a letter")

guesses = ''

turns = 6


while turns > 0:
	
	# Number of times the player fails
	failed = 0
	for char in word:
		if char in guesses:
			print(char)	
		else:
			print("_")
			failed += 1 #Increase in failures by 1
   
	if failed == 0:
		# Player will win the game if failure is 0
		print("You Win")		
		print("The word is: ", word)
		break
	
	guess = input("Guess another letter:") #Enter another letter after getting it wrong
	guesses += guess

	if guess not in word:
		
		turns -= 1
		
		print("Wrong") #letter doesnt match word in guess
		
		# turns remaining
		print("You have", + turns, 'more guesses')
			
		if turns == 0: # Depleted number of turns available.
			print("You Loose")
