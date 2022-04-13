
def _init_(self, string):
  self.string = string

def _str_(self):
  if self.string:
    print(_str_)

def vowels(self):
  vowels = ["a","e","i","o","u"]
  for i in _str_:
    count = int(vowels)
    if count <= 5:
      print(count)
    else:
      print("Many")

def bothEnds(self):
  if _str_ > 2:
    print(_str_[:2]+_str_[:-2])
  else:
    print([])

def fixStart(self):
  parameter_char = len(_str_)
  #parameter_fixed = parameter_char.replace(1:1)
  if parameter_char < 2:
    return parameter_char
  else:
    return parameter_fixed

def asciisum(self):
  str1 = _str_
  li = []
  li[:0]=str1
  print(li)
  result = []
  for i in range(len(li)):
    result.append(ord(li[i]))
    result = list(set(result))
  print(result)
  done = sum(result)
  print(done)

def cipher(self):
  value = _str_
  for x in range (0,len(value)):
    cipher_final+=(chr(ord(value[x])+1))
  print(cipher_final)