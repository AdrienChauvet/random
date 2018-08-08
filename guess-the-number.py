from random import randrange

mini = 0
maxi = 100
number = randrange(mini, maxi + 1, 1)
liste = list(range(maxi + 1))

print("\n\t*** Guess the number! ***\n")

print("What is the number, between {0} and {1} included?\n".format(mini, maxi))

while True:
	a = int(input("\tYour choice: "))

	if a < mini or a > maxi:
		print("You must enter a number between 0 and 100 included.\n")
		continue
	if a == number:
		print("Congratulations!")
		break
	elif a < number:
		print("Too low!")
		continue
	else:
		print("Too high!")