a = 0 
b = 1 
print(a)
print(b)
count = 0
while count <10:
  a,b = b, a+b
  print(b)
  count += 1