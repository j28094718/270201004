age = {}
while True: 
  name = input("Enter the name:")
  if name == "exit":
    break
  else : 
    ages = int(input("Enter the age"))
  age[name] = ages 
for i,j in age.items():
  if j >= 18: 
    print(i)