from utils import utils
from math import sqrt

def task():

  param_a = utils.enterFloatParams('Bitte gib zuerst den Parameter a an: ')
  param_b = utils.enterFloatParams('Bitte gib zuerst den Parameter b an: ')
  param_c = utils.enterFloatParams('Bitte gib zuerst den Parameter c an: ')

  steps = utils.enterIntParams('Bitte gib eine Schrittweite an: ')

  interval_min = utils.enterIntParams('Bitte gib nun den minimalen Intervallwert an ( ?<x ): ')
  interval_max = utils.enterIntParams('Bitte gib nun den maximalen Intervallwert an ( x<? ): ')

  r = range (interval_min, interval_max, steps)
  
  for x in r:
    l = param_a * x * x + param_b * x + param_c
    
    print(x, l)
    
    
  return True 