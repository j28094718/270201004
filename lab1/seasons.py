month = int(input("enter the month:"))
day = int(input("enter the day:"))
if (month == 3 and day >= 20) or (month == 4) (month ==5) or (month ==6 and day < 21): 
  print("Spring")
elif (month == 6 and day >= 21) or (month == 7) or (month == 8) or (month == 9 and day < 22):
  print("Summer")
elif (month == 9 and day >= 22) or (month == 10) or (month == 11) or (month == 12 and day <21): 
  print("Fall")
elif (month == 12 and day >= 21) or (month == 1) or (month == 2) or (month == 3 and day < 20): 
  print("Winter")
  
