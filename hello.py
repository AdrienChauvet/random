name = input("What is your name?\n")
age = int(input("How old are you?\n"))

if age < 18:
	print("Sorry {}, you're too young to play the game.".format(name.capitalize()))
elif age > 90:
	print("Welcome to the game Master {}.".format(name.capitalize()))
else:
	print("Welcome to the game, {}.".format(name.capitalize()))