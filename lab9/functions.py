def harmonic_sum(n):
  if n == 1: 
    return 1 
  else : 
    return (1/n) + harmonic_sum(n-1)