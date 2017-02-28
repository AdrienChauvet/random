from random import randrange

while True:
	print("\n\t*** Dice Rolling Simulator ***\n")
	print("\tRoll: 1\tQuit: 2\n")

	a = int(input())

	if a == 2:
		break
	else:
		print("\n\tResult:", randrange(1, 7, 1), end="\n")
