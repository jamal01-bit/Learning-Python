print('=== Shopping List ===')
print('Options: add | remove | view | quit')

shoppinglist = []
while True:
 choice = input('> ').lower()
 if (choice == 'add'):
  item = input('Add item: ').lower()
  shoppinglist.append(item)
  print(f'{item} added')
 elif (choice == 'remove'):
  item = input('Remove item: ').lower()
  if item in shoppinglist:
   shoppinglist.remove(item)
   print(f'{item} removed')
  else:
   print('item not in shopping list')
 elif (choice == 'view'):
  if (len(shoppinglist) == 1): 
   print(f'Your list ({len(shoppinglist)}) item')
  else:
   print(f'Your list ({len(shoppinglist)}) items')
  for i, item in enumerate(shoppinglist, 1):
   print(f'{i}. {item}')
 elif (choice == 'quit'):
  print(shoppinglist)
  print('Goodbye')
  break
 else:
  print("That isn't a valid option please try again")
