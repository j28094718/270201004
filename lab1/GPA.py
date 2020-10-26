a = float(input("enter the GPA:"))
b = int(input("enter the numbers of lectures:"))
if a >= 2.0 and b >= 47: 
  print("Graduated")
elif a >= 2.0 and b < 47: 
  print("Not enough number of lectures.")
elif a < 2.0 and b >= 47: 
  print("Not enough GPA")
else : 
  print("Not enough number of lectures and GPA")
