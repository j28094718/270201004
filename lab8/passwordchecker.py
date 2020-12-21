def passwordchecker(password):
  for i in password:
    if i.isspace() == True:
      print('Password is invalid.')
      return False 
  if len(password) < 8:
    print('Password is invalid.')
    return False 
  for i in password: 
    empty_set = set()
    if i.isalpha() == True: 
      empty_set.add('alpha')
    elif i.isdigit() == True: 
      empty_set.add('digit')
    else : pass  
  print('security level is',len(empty_set))
  print(empty_set)
passwordchecker('5616455vbc')