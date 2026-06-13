import random
print("I'm thinking of a number between 1 and 100")
tries = 0
number = random.randint(1,101)
guess = 0
while (guess != number):
 guess = int(input('Guess: '))
 if (guess < number):
  print('Too low')
  tries += 1
 elif (guess > number):
  print('Too high')
  tries += 1
 else:
  tries += 1
print(f'Correct!, You got it in {tries} guesses')
 
