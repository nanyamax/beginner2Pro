name = input("What is your name: ")
print('welcome', name,'to this adventure!' ) 
answer = input('You are at the end of a dirt road, you can either go left or right. Which way would you like to go? ').lower()

if answer == 'left':
  answer2 = input('You chose the path to the river, you can either walk around it or swim across. Choose one option, walk or swim? ').lower()
  if answer2 == 'walk':
    print('Oops, you lost your way in the dessert up ahead. Game over')
  elif answer2 == 'swim':
    print('uh-oh , you were eaten by an alligator. Game over')
  else:
    print('invalid response. Game over')
elif answer == 'right':
  answer3 = input('There is a bridge up ahead and it looks old and wobbly. would you like to cross or go back? cross/back ')
  if answer3 == 'cross':
    print('Congratulations you crossed over. You win!!!')
  elif answer3 == 'back':
    print("You turned into a pillar of salt. Game over")
  else:
    print('invalid response. Game over')


else:
  print('not a valid response. Game over')

print('Thank you for trying', name)