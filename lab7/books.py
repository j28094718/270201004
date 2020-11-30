books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
empty_list = []
for i in books:
  for a in i: 
    if a in empty_list: 
      pass 
    else : 
      empty_list.append(a)
  book_dict[i] = (len(i), len(empty_list), (len(i) + len(empty_list)) / 2)
print(book_dict)
