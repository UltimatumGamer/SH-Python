from utils import utils
from math import sqrt

def task():

  param_a = utils.enterFloatParams('Bitte gib zuerst den Parameter a an: ')
  param_b = utils.enterFloatParams('Bitte gib zuerst den Parameter b an: ')
  param_c = utils.enterFloatParams('Bitte gib zuerst den Parameter c an: ')

  steps = utils.enterFloatParams('Bitte gib eine Schrittweite an: ')

  print("Bitte geben sie nun den Intervall an.")
  interval_min = utils.enterFloatParams('Bitte gib nun den minimalen Intervallwert an ( ?<x ): ')
  interval_max = utils.enterFloatParams('Bitte gib nun den maximalen Intervallwert an ( x<? ): ')

  
  if param_a != 0.0:
      param_delta = param_b * param_b - 4.0 * param_a * param_c
      if param_delta > 0.0:
          x1 = (-param_b + sqrt(param_delta)) / (2.0 * param_a)
          x2 = (-param_b - sqrt(param_delta)) / (2.0 * param_a)
          # Die Gleichung hat zwei verschiedene reelle Lösungen:
          print("x1 =", x1, "     ", "x2 =", x2)
      elif param_delta == 0.0:
          # Die Gleichung hat eine reelle Lösung
          x1 = -param_b / (2.0 * param_a)
          print("x1 = x2 =", x1)
      else:
          False
          # Die Gleichung hat keine reelle Lösungen.
  else:
      if param_b != 0.0:
          x = -param_c / param_b
          # Die Gleichung ist linear und hat somit eine Lösung:
          print("x =", x)
      else:
          if param_c != 0.0:
              False
              # Die Gleichung ist unlösbar!
          else:
              False
              # Die Gleichung hat unendlich viele Lösungen!



  print('1')
  return False 