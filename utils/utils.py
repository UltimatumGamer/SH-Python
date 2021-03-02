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

# Wiederholt sich bis Parameter eine Zahl ist
def enterFloatParams(text, *param):
    while True:
        param_input = input(str(text).format(param))
        if isfloat(param_input):
            return float(param_input)
        else:
            print("Fehler: Bitte gib eine gültige Zahl an.")
