from utils import utils

def task():
	input = utils.enterIntParams(
	    "Bitte geben sie eine ISBN Nummer zum verifizeren an: ")
	list = [int(x) for x in str(input)]
	last = list.pop()
	print(list)
	m = False
	for y in range(0, len(list)):
		if (m == True):
			list[y] = list[y] * 3
			m = False
		else:
			m = True

	print(list)
	summe = sum(list)
	if len(list) == 9:
		check = 11 - (summe % 11)
	else:
		check = 10 - (summe % 10)

	if (check == last):
		print("Die ISBN ist gültig")
	else:
		print("Die ISBN ist ungültig")

	return True
