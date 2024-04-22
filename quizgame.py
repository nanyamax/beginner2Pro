print("It's time to play a game")
play_game = input('Start game: ' )

if play_game.lower() != "yes":
  quit()
print("let's get started")

score = 0
attempt = 0
max_attempt = 3
while attempt < max_attempt:
   output = input('What does AI stand for? ')
   attempt += 1
   if output.lower() == 'artificial intelligence':
     print('correct')
     score += 1
     break
   else:
     if attempt == max_attempt:
      print('Maximum attempts exceeded')
      break
     else:
       print('incorrect, Try again')

attempt = 0
while attempt < max_attempt:
   output = input('What does CPU stand for? ')
   attempt += 1
   if output.lower() == 'central processing unit':
     print('correct')
     score += 1
     break
   else:
     if attempt == max_attempt:
      print('Maximum attempts exceeded')
     else:
       print('incorrect, Try again')

attempt = 0
while attempt < max_attempt:
   output = input('What does GPU stand for? ')
   attempt += 1
   if output.lower() == 'graphics processing unit':
     print('correct')
     score += 1
     break
   else:
     if attempt == max_attempt:
      print('Maximum attempts exceeded')
     else:
       print('incorrect, Try again')

attempt = 0
while attempt < max_attempt:
   output = input('What does RAM stand for? ')
   attempt += 1
   if output.lower() == 'random access memory':
     print('correct')
     score += 1
     break
   else:
     if attempt == max_attempt:
      print('Maximum attempts exceeded')
     else:
       print('incorrect, Try again')

attempt = 0
while attempt < max_attempt:
   output = input('What does ROM stand for? ')
   attempt += 1
   if output.lower() == 'read only memory':
     print('correct')
     score += 1
     break
   else:
     if attempt == max_attempt:
      print('Maximum attempts exceeded')
     else:
       print('incorrect, Try again')

print(f'you answered {score} questions correctly')