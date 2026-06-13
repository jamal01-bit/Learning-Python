tasks = []
while True:
 print('\n--- TO-DO LIST ---')
 print('1. View Tasks')
 print('2. Add Task')
 print('3. Delete Task')
 print('4. Exit\n')
 try:
  option = int(input('Choose an option (1-4): '))
 except ValueError:
  print('Invalid option, please choose a number between 1 and 4')
  continue 
 if option == 1:
  if not tasks:
   print('You have no tasks')
  else:
   print('Current Tasks:')
   for i, task in enumerate(tasks):
    print(f'{i+1}. {task}')
 elif option == 2:
   new_task = input('Add task: ')
   tasks.append(new_task)
 elif option == 3:
   remove_task = int(input('\nEnter the number of the task you would like to delete: '))
   try:
    tasks.pop(remove_task - 1)
    print(f'\'{tasks.pop(remove_task - 1)}\' has been deleted')
   except ValueError:
    print('Error: Not a valid input')
   except IndexError:
    print('Error: There aren\'t that many tasks')
 elif option == 4:
  break
 else:
   print('Error: Invalid option, please choose between 1 and 4')
