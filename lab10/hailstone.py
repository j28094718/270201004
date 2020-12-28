def hailstone(n):
  if n == 1:
    print(int(n))
    return n   
  elif n % 2 == 0:
    if n/2 == 1:
      return hailstone(n/2) 
    else : 
      print(int(n/2))
      return hailstone(n/2) 
  elif n % 2 != 0:
    print(int(3*n+1))
    return hailstone((3*n)+1)