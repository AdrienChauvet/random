from random import randrange

liste = ['test', 'amande', 'fluffy', 'disco', 'baloo', 'zinc', 'forest']

word = randrange(0, len(liste), 1)

guesses_left = 5
letters = []

def guess_length(a):
	if len(a) == 0 or len(a) > 1:
		return False
	else:
		return True

def letter_in_word(a):
	x = liste[word].count(a)
	if  x > 0:
		print("The letter '{}' appears {} time(s) in the word.".format(a, x))
		letters.append(a)
		for i in letters:
			print(i)
	else:
		print("The letter '{}' doesn't appear in the word.".format(a))

print ("\n\t*** Hangman ***")

while guesses_left > 0:

	guess = input("Enter a letter: ")
	guesses_left -= 1

	if guess_length(guess):
		letter_in_word(guess)
		a = input("What's the word? ")
		if a == liste[word]:
			print("Congratulations!")
			break
		else:
			print("Nope!")
	else:
		print("Please enter a single letter.")
	print ("{} guesses left.".format(guesses_left))