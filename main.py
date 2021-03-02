from tasks import Aufgabe1 as t1
from tasks import Aufgabe2 as t2
from tasks import Aufgabe3 as t3
from tasks import Aufgabe4 as t4
from utils import utils

setTask = None

def task(param):
  if setTask == 1:
    # Aufgabe 1
    t1.task()
  elif setTask == 2:
    # Aufgabe 2
    t2.task()
  elif setTask == 3:
    # Aufgabe 3
    t3.task()
  elif setTask == 4:
    # Aufgabe 4
    t4.task()
  else:
    return False


# Wenn aus irgendeinem Grund man das 
# Select-Menu nicht benutzen kann, 
# können sie die nächste Zeile auskommentieren

#setTask = 1

"""
Aufgabenstellung zur Wiederholung und Übung von Schleifen

Erstellen Sie das Struktogramm und das Programm in PYTHON für folgende Probleme Nutzen Sie für den Programmtest und die Implementierung auch einen Debugger.
1.	Ausgabe einer Wertetabelle einer quadratischen Funktion (Der Nutzer soll die Parameter, das Intervall und die Schittweite frei wählen).
2.	Berechnung der Fibonacci-Zahlen, bis eine vom Nutzer angegebene Anzahl erreicht wird.
3.	Berechnung der Anzahl der Permutationen mit einer Schleife. (Bsp. Anzahl der möglichen Anordnungen)
4.	Berechnung der Anzahl der Kombinationen (Bsp: Wie vieleMöglichkeiten gibt es, aus 10 Personen 3 auszuwählen).

"""

if setTask != None:
  task(setTask)
else:
  while setTask == None:
      print("Welche Aufgabe soll aufgerufen werden? ")
      inputTask = input("Aufgabe: ")
      if utils.isfloat(inputTask):
        setTask = int(inputTask)

  task(setTask)