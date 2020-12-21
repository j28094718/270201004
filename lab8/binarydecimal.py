def binarytodecimal(binary):
  n = 0
  m = 0 
  binary = str(binary)
  binary = binary[::-1]
  for i in binary:
    m += int(i) * ((2)**n)
    n += 1 
  print(m) 
binarytodecimal(110101)
def decimaltobinary(number):
  e_str = ''
  liste = list()
  b = number // 2 
  k = number % 2
  liste.append(b)
  while b >= 2:
    b = b // 2
    liste.append(b)
  liste.append(k)
  for i in liste:
    e_str = e_str + str(i)
  print(e_str)
decimaltobinary(53)