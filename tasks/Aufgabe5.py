from utils import utils

def fibo(n):
  # print(n)
  if(n==1):
    return (0)
  elif(n==2):
    return (1)
  else:
    return fibo(n-1) + fibo(n-2)
  
def task():

  x = utils.enterIntParams('Wie viele Fibonacci-Zahlen sollen angezeigt werden?  ')
  print(fibo(x))
  return True

