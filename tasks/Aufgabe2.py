from utils import utils


def task():

	n1 = 1
	n2 = 1

	count = 0

	countTo = utils.enterIntParams(
	    'Wie viele Fibonacci-Zahlen sollen angezeigt werden?  ')

	if countTo <= 0:
		print("Bitte gib eine positve Zahl an")
	else:
		while count < countTo:
			print(str(count + 1) + " " + str(n1))
			nth = n1 + n2
			n1 = n2
			n2 = nth
			count += 1

	return True
