from utils import utils

def task():
  
  data = list(range(1,10))
  i = 0;
  for p in utils.permutation(data): 
    print(p)
    i += 1
  
  print(i)
  # print('3')
  return False 