a = float(input("enter the first value:"))
b = float(input("enter the second value:"))
c = float(input("enter the third value:"))
if (a > b and b > c) or (a > c and c > b): 
  print("greatest value is", a)
elif (b > a and a > c) or (b > c and c > a): 
  print("greatest value is", b)
elif (c > a and a > b) or (c > b and b > c): 
  print("greatest value is", c)
