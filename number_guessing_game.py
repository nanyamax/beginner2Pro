import random

# difference btw randrage and randint 
#randrange does not generate/include the stop specified number.
#randint includes the stop specified number when generating random numbers.


pick_a_number = input('Type a number: ')
if pick_a_number.isdigit():
  pick_a_number = int(pick_a_number)
  if pick_a_number <= 0:
    print('number must be greater than 0')
    quit()
else:
  print('Please type a number next time')
  quit()

random_number = random.randrange(0, pick_a_number)
guesses = 0

while True:
  guesses += 1
  user_guess = input('Guess a number: ')
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print('Please type a number')
    continue

  if user_guess == random_number:
    print('You got it right')
    break
  elif user_guess < random_number:
    print('Your guess is lower than the number')
  else:
    print('Your guess is higher than the number')

print(f'you got it in  {guesses} guesses' )