numberlist = []
while True:
 number = input("Enter a number (or 'done' to finish): ")
 if (number == 'done'):
  break
 else:
  number = float(number)
  numberlist.append(number)
print('--- Stats ---')
print(f'Count: {len(numberlist)}')
print(f'Total: {sum(numberlist)}')
print(f'Highest: {max(numberlist)}')
print(f'Lowest: {min(numberlist)}')
print(f'Average: {float(sum(numberlist) / len(numberlist))}') 

