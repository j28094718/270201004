a = int(input("enter the a:"))
b = int(input("enter the b:"))
c = int(input("enter the c:"))
discriminant = ((b ** 2) - 4 * a * c)
if discriminant > 0: 
  print("there are two real roots.")
elif discriminant == 0: 
  print("there is one real root.")
else : 
  print("there are two complex roots.")