
#import module random(to change the computer choises)
import random
#array with the computer choises
computer_choice = random.choice(
                [
                'scissor',
                'paper',
                'rock'
                 ]
             )
             
user_choice = input('Choose between: rock, scissor or paper.\n')

#conditional to define who is the winner
if user_choice == computer_choice:
    print('TIE, computer choice ' + computer_choice + ' too!');
elif user_choice == 'rock' and computer_choice == 'scissor':
    print('WIN, computer had ' + computer_choice + '!')
elif user_choice == 'scissor' and computer_choice == 'paper':
    print('WIN, computer had ' + computer_choice + '!')   
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN, computer had ' + computer_choice + '!')
else:
    print('Computer choose ' + computer_choice + ' You lose! :( computer wins!')