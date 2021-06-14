from utils import utils

def task():
  
  param_count = utils.enterIntParams('Bitte gib eine Zahl an: ')
  i = 1
  s = 1
  while i < param_count:
    s = s * (i+1)
    i += 1 
    
    
  print(s)
  
  # print('3')
  return False 