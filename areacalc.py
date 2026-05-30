print('================')
print('Area Calculator')
print('================')
print()
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')

shape = int(input('Which shape: '))

if shape == 1:
 base = int(input('Base: '))
 height = int(input('Height: '))
 area = (base * height) / 2
elif shape == 2:
 base = int(input('Base: '))
 height = int(input('Height: '))
 area = base * height
elif shape == 3:
 side = int(input('Side: '))
 area = side ** 2
elif shape == 4:
 radius = int(input('Radius: '))
 area = (radius * radius) * 3.14
else:
 print('That is not a valid shape') 

print(f'The area is {area}cm^2') 
