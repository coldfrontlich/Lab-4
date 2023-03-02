import random
import string

def key_creationing():
  letters = string.ascii_uppercase
  digits = string.digits
  list = []
  result = ""

  for i in range(4):
    list.append(random.choice(letters))
    list.append(random.choice(letters))
    list.append(random.choice(letters))
    list.append(random.choice(digits))
    random.shuffle(list)
    result += "".join(list) + "-"
    list.clear()
  return result[0:-1]
