def overlap(a,b):
  print(a)
  print(b)
  print('their overlaps are:',end = '')
  for i in a: 
    if i in b:
      print(i,end = ',')
    else : 
      pass 
liste1 = [1,2,3,4,60,41,40,89]
liste2 = [1,4,5,41,87]
overlap(liste1,liste2)