month = int(input("enter the month:"))
day = int(input("enter the day:"))
if (month == 3 and day >= 20) or (3 < month < 6) or (month ==6 and day < 21): 
  print("Spring")
elif (month == 6 and day >= 21) or (6< month <9) or (month == 9 and day < 22):
  print("Summer")
elif (month == 9 and day >= 22) or (9 < month < 12) or (month == 12 and day <21): 
  print("Fall")
elif (month == 12 and day >= 21) or (12 < month < 3) or (month == 3 and day < 20): 
  print("Winter")
