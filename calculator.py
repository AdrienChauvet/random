choicelist = [i for i in range(5)]

while True:
	print("\n****  CALCULATOR  ****\n")
	print("\t+    1")
	print("\t-    2")
	print("\t*    3")
	print("\t/    4")
	print("\tquit 5\n")

	op = int(input("Choose an operation: "))

	if op == 5:
		break
	if op not in choicelist:
		print("\n\tUnexpected choice. Try again!")
		continue

	a = float(input("\n\tA = "))
	b = float(input("\n\tB = "))

	if op == 1:
		result = a + b
	elif op == 2:
		result = a - b
	elif op == 3:
		result = a * b
	elif op == 4:
		if a == 0 or b == 0:
			print("Null division!\n")
			continue
		result = a / b

	print("\n\tResult =", result)

print("\n\tBye!\n")