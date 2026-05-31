def get_item(x):
 if x == 1:
   print('Cheeseburger')
 elif x == 2:
   print('Fries')
 elif x == 3:
   print('Soda')
 elif x == 4:
   print('Ice Cream')
 elif x == 5:
   print('Cookie')

def welcome():
  print('Cheesburger')
  print('Fries')
  print('Soda')
  print('Ice cream')
  print('Cookie')   

welcome()
option = int(input('What would you like to order: '))
get_item(option)
