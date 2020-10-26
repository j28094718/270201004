old = int(input("Please enter your age:"))
ticket_price = 3 
if old > 60 or old < 6:
  ticket_price = 0
  print(ticket_price) 
elif  old < 18 and old > 6: 
  ticket_price = 3 * (0.5)
  print(ticket_price)
else : 
  print(ticket_price)
