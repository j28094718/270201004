tim = int(input("Enter how many times you want to add:")) 
even = 0 
odd = 0 
while tim > 0:
  number = int(input("Enter the number:"))
  tim -= 1 
  if number // 2 == 0: 
    even += 1 
  else : 
    odd += 1 
print(even / (odd + even))