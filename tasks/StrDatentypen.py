from random import randint


def task():

	L = []
	for x in range(0, 6):
		y = randint(1, 49)
		if (y not in L):
			L.append(y)
		else:
			print("-")
			x -= 1

	print("Lottozahlen: " + str(L))
	print("Superzahl: " + str(randint(0, 9)))
	return True
