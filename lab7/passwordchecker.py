password = input("enter the password:")
if len(password) >= 8: 
  if password.isdigit() == False:
    if password.isalpha() == False: 
      if password.isupper() == False: 
        if password.islower() == False:
            print("password is valid.")
        else : 
            print("password is invalid")
      else : 
          print("password is invalid")
    else : 
        print("password is invalid")
  else : 
      print("password is invalid")
else : 
  print("password is invalid.")