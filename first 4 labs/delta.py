a = int(input("enter the a:"))
b = int(input("enter the b:"))
c = int(input("enter the c:"))
discriminant = ((b ** 2) - 4 * a * c)
if discriminant > 0: 
  x1 = (-1 * b) + (disc ** 0.5) / (2 * a)
  x2 = (-1 * b) - (disc ** 0.5) / (2 * a)
  print("there are two real roots.")
  print("and roots are", x1, x2)
elif discriminant == 0: 
  x = (-1 * b) / (2 * a)
  print("there is one real root.")
  print("and the root is", x)
else : 
  print("there are two complex roots.")