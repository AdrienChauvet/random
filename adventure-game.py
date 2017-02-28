print("\n\t\t*** THE DUNGEON ***\n\nWelcome to the dungeon! Behold its magnificent map!\n")

plan = """\
\t\t   | 1 |
\t\t| 2  0  3 |
\t\t   | 4 |
"""
print(plan)

room = 0

room_message = "You entered the room {0}.\nType {1} to exit."

def sortie(a):
	while a != exit:
		a = input("Type a direction: ")
		if a != exit:
			print("There is a wall, you can't go in this direction.")

while True:
	a = input("You are in the central hall. Type a direction (up, down, right, left) to enter a room: ")

	if a == 'q':
		break

	if a not in ('up', 'down', 'right', 'left'):
		print("That's not a direction.")
		continue
	else:
		if a == 'up':
			room = 1
			exit = 'down'
			print(room_message.format(room, exit))
			sortie(a)
			continue
		if a == 'down':
			room = 4
			exit = 'up'
			print(room_message.format(room, exit))
			sortie(a)
			continue
		if a == 'right':
			room = 3
			exit = 'left'
			print(room_message.format(room, exit))
			sortie(a)
			continue
		if a == 'left':
			room = 2
			exit = 'right'
			print(room_message.format(room, exit))
			sortie(a)
			continue

	print("You're back in the central hall.")

print("You left the game.")
