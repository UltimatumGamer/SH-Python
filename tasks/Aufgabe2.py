from utils import utils

def task():
  
  n1=0;
  n2=1;
  
  count = 0;
  
  nterms = utils.enterIntParams('Wie viele Fibonacci-Zahlen sollen angezeigt werden?  ')
  
  if nterms <= 0:
   print("Bitte gib eine positve Zahl an")
  elif nterms == 1:
   print(n1)
  else:
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
    
  
  print('2')
  return True 