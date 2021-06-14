from utils import utils
from random import randint


def find(L):
  global erg;
  schluessel = int(input("Geben sie eine Zahl ein: "))
  L.sort()
  u = 0
  o = len(L) - 1
  while u <= o:
  	m = (u + o) // 2
  	if (schluessel == L[m]):
      erg = m
  		return True
  	if (L[m] <= schluessel):
  		u = m + 1
  	else:
  		o = m - 1
  return False


# Liste erstellen
def createList(length, min, max):
	L = []
	for i in range(0, length):
		L.append(randint(min, max))
	return L


def task():

	# Zufällige Liste oder die Liste an der Tafel
	if (True):
		# Erzeugen einer Liste (Länge, Min, Max)
		liste = createList(100, 0, 100)
		print(liste)
		x = find(liste)
		print(x)
	else:
		x = find([5, 16, 4, 6, 3, 1, 15, 10, 2, 8, 9, 7, 11, 13, 14, 12])
		print(x)
