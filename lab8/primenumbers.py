def is_prime(value): 
  y = 2
  if value == 1:
    return False
  while y < value: 
    if value % y == 0:
      break 
      return False 
    else : 
      value / y 
      y += 1 
  if y == value: 
    return True 
  else : 
    pass 
is_prime(1)
def print_primes_between(a,b):
  for i in range(a,b):
    if is_prime(i) == True:
      print(i)
    else: 
      pass