def isDefined(var):
  try:
    var
  except NameError:
    return False
  else:
    return True

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def enterFloatParams(text, *param):
    while True:
        param_input = input(str(text).format(*param))
        if isfloat(param_input):
            return float(param_input)
        else:
            print("Fehler: Bitte gib eine gültige Zahl an.")

def enterIntParams(text, *param):
    while True:
        param_input = input(str(text).format(param))
        if isint(param_input):
            return int(param_input)
        else:
            print("Fehler: Bitte gib eine gültige Zahl an.")

def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 