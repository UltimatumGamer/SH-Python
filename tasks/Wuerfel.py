from random import randint


def task():

	wuerfel_min = 1
	wuerfel_max = 6

	anzahl_der_würfe = 10000

	E = []

	while len(E) < anzahl_der_würfe:
		y = randint(wuerfel_min, wuerfel_max)
		E.append(y)

	print(E)
	t = (E.count(1) + E.count(2) + E.count(3) + E.count(4) + E.count(5) +
	     E.count(6))
	print("Total: " + str(t))

	sum = 0
	count = 0

	for i in E:
		sum += i
		count += 1

	print(str(sum / count))
	for x in range(wuerfel_min, wuerfel_max + 1):
		print(
		    str(x) + ": " + str(E.count(x)) + "/" + str(anzahl_der_würfe) +
		    " | " + str(E.count(x) / anzahl_der_würfe * 100) + "%")

	return True
