bill = float(input('Enter bill amount: '))
tippercentage = float(input('Enter tip percentage: '))
tip = (tippercentage / 100) * bill
tip = round(tip, 2)
print(f'Tip amount: {tip}')
print(f'Total to pay: {bill + tip}')
