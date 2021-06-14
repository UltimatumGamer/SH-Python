from utils import utils

def task():
  word = input("Geben sie ein Wort ein: ")

  replace = ['a','e','i','o','u']
  letterReplace = 'ö'
  
  for x in replace:
    word = word.replace(x, letterReplace)
    
  print(word)
  
  