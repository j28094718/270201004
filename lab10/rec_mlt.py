def it_mlt_x3(n):
  c = 0
  if n == 0 or n == 1:
    return n * 3 
  else : 
    return it_mlt_x3(n-1) + 3 
print(it_mlt_x3(12))